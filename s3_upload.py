import boto3

class s3Uploader:

    def __init__(self, s3_path):
        self.s3_path = s3_path
        
 
    def uploadS3(self, file_Name, file_Path, bucket_Name):
        try:
            s3 = boto3.resource('s3')
            
            # Prepends the "subfolder path" to the filename
            s3_Full_Name = self.s3_path + file_Name

            # Uploads the given file using a managed uploader, which will split up large
            # files automatically and upload parts in parallel.
            s3.Bucket(bucket_Name).upload_file(file_Path, s3_Full_Name)
            print("Uploaded file: %s" % file_Name)

            # This will make this file open to the public in S3. Anyone will be able to download it.
            # Make sure this is what you want!!!!!
            s3.ObjectAcl(bucket_Name, s3_Full_Name).put(ACL='public-read')
        except Exception as error_message:
            raise Exception(error_message)