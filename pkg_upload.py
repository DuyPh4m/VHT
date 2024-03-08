from time import sleep
import boto3
from botocore.client import Config
import tarfile
import os
from dotenv import load_dotenv
from datetime import datetime
from unzip_register import copy_to_local

load_dotenv()

def upload_object_to_minio(folder_path, bucket_name):
    s3 = boto3.client(
        's3',
        endpoint_url=os.environ['MINIO_URL'],  # replace with your Minio server
        aws_access_key_id=os.environ['MINIO_ACCESS_KEY'],  # replace with your access key
        aws_secret_access_key=os.environ['MINIO_SECRET_KEY'],  # replace with your secret key
        config=Config(signature_version='s3v4')
    )

    folder_name = os.path.basename(folder_path)  # name of the folder to upload
    tarball_name = f"./{folder_name}.tar.gz"  # temporary tarball file
    object_name = f"{datetime.now().strftime('%H_%M_%S')}_{folder_name}.tar.gz"  # name of the object in the bucket

    # print(folder_name)
    # print(object_name)
    # print(tarball_name)
    with tarfile.open(tarball_name, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))

    try:
        s3.upload_file(tarball_name, bucket_name, object_name)
        print(f"{folder_path} uploaded to {bucket_name} on Minio server as {object_name}")
    except Exception as e:
        print(f"Error uploading folder: {e}")

    os.remove(tarball_name) # clean up the temporary tarball file

# usage
for i in range(5):
    upload_object_to_minio('/home/duypham/Documents/Project/VHT/flyte_demo/workflows', 'dev')
    sleep(3)

# path = "test/abc/duy"
# print(os.path.basename(path))