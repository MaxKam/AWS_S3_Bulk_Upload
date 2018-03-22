import os
import configparser
from s3Upload import s3Uploader

config = configparser.ConfigParser()
config.read("settings.txt")

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
        file_name = file_item.rsplit("\\", 2) # Gets file name and parent directory from full path
        file_name = file_name[1] + "/" + file_name[2]
        awsS3.uploadS3(file_name, file_item, bucket_name)

def main():
    file_list = list_files(folder_path)
    upload_files(file_list)

if __name__ == "__main__":
    main()
