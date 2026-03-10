import boto3
import uuid

# Create a S# bucket
s3_client= boto3.client("s3")

# Function to create an S3 bucket
def manage_s3_bucket():
    # Create an S3 bucket
    bucket_name= f"my-boto3-bucket-{uuid.uuid4().hex[:6]}"
    s3_client.create_bucket(Bucket=bucket_name)

    # Upload a file  to the s3 bucket
    file_name= "infrastructure-provider-message.txt"
    s3_client.upload_file(file_name, bucket_name, file_name)

    # list objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    for obj in response.get("Contents", []):
        print("Objects: " + obj["Key"])

# Call the function to manage the s3 bucket
manage_s3_bucket()