"""
This is a script to take backup from a local to AWS s
"""
import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name, region):
    s3.create_bucket(
        Bucket=bucket_name,  
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print("Bucket created successfully")

def upload_backup(s3,file_name,bucket_name,Key_name) :
    data = open(file_name,'rb')
    s3.Bucket(bucket_name).put_object(Key = Key_name,Body= data)
    print("Backup uploaded sucessfully")

bucket_name = "python-for-devops-001"  
region = 'eu-north-1'

# create_bucket(s3,bucket_name, region)  
# show_buckets(s3)

file_name = r"C:\Users\utkar\pythonbase\backups\backup_2025-08-13.tar.gz"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")