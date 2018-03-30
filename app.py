import os
import configparser
from datetime import datetime
from s3_upload import s3Uploader

config = configparser.ConfigParser()
config.read("settings.ini")

folder_path = config.get("DEFAULT", "folder_path")
bucket_name = config.get("DEFAULT", "bucket_name")
s3_path = config.get("DEFAULT", "s3_path")

awsS3 = s3Uploader(s3_path)

def list_files(dir):
    file_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            file_list.append(os.path.join(root, name))
    return file_list

def upload_files(file_list):
    for file_item in file_list:
        try:
            file_name = file_item.rsplit("\\", 2) # Gets file name and parent directory from full path
            file_name = file_name[1] + "/" + file_name[2]
            awsS3.uploadS3(file_name, file_item, bucket_name)
        except Exception as error_message:
            error_file = open("aws_upload_errors.txt","a+")
            current_time = datetime.now().isoformat('_', timespec='seconds')
            error_file.write('%s -- %s: \n %s \n' % (current_time, file_item, error_message))
            error_file.close()

def main():
    file_list = list_files(folder_path)
    upload_files(file_list)

if __name__ == "__main__":
    main()
