import boto3
import json

# Create IAM client
iam = boto3.client('iam')

# Trust policy for EC2
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create IAM role
iam.create_role(
    RoleName='EC2AccessRole',
    AssumeRolePolicyDocument=json.dumps(assume_role_policy)
)

# Attach AWS managed policy to the role
iam.attach_role_policy(
    RoleName='EC2AccessRole',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

print("IAM Role created and policy attached successfully")