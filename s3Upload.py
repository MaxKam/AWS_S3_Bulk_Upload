import boto3

class s3Uploader:

    def __init__(self):
        # Create an S3 client
        s3 = boto3.client('s3')

 
    def uploadS3(self, filePath, bucketName, s3FileName):
        
        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        s3.upload_file(filePath, bucket_name, filename)