import boto3

#create a boto3 EC2 client , for the us-east-1, region
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Function to launch EC2 instance
def create_ec2_instance():
    response = ec2_client.run_instances(
        ImageId='ami-02dfbd4ff395f2a1b', #AMI ID
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='key-ec2',
        SecurityGroupIds=['sg-08c42ceeb9575xxxx'], # Security group
        SubnetId='subnet-0a5bed300335xxxxx',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'AutomatedInstance'
                }
            ]
        }
    ]
)
    # Print the Instances ID of the launched EC2 instance
    print("Instance_ID:", response['Instances'] [0] ['InstanceId'])

# Call the function to create the ec2 instance
create_ec2_instance()