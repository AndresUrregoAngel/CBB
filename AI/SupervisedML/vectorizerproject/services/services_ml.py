import boto3
import os


class services(object):
    
    def __init__(self,bucket=None,vectkey=None):
        self.bucket = os.environ["bucket"]
        self.vectkey = os.environ["vectkey"]
        
    def storeons3(self,vectorizer):
        
        client = boto3.client("s3")
        response = client.put_object(
            Bucket = self.bucket,
            Key = self.vectkey,
            Body = vectorizer
            )
            
        print(response['ResponseMetadata']['HTTPStatusCode'])
        
    def getfroms3(self,dir_path):
        
        client = boto3.client("s3")
        
        response = client.download_file(self.bucket,self.vectkey,dir_path+"/"+self.vectkey)
        
        print("The file has been download successfully at local path")