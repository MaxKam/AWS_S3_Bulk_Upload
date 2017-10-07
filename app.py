import os
import ConfigParser
from s3Upload import s3Uploader

config = ConfigParser.ConfigParser()
config.read("settings.txt")

folder_path = config.get("DEFAULT", "folder_path")
bucket_name = config.get("DEFAULT", "bucket_name")
s3_path = config.get("DEFAULT", "s3_path")

awsS3 = s3Uploader()

for file_name in os.listdir(folder_path):
    awsS3.uploadS3(file_name, folder_path + file_name, bucket_name)

