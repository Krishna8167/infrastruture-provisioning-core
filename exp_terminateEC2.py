import boto3

# create an ec2 client
ec2_client = boto3.client( 'ec2')

# Function to list and terminate an ec2 instance
def terminate_instance():
    # List all running instances
    response = ec2_client.describe_instances()

    # Get the instance Id of the first runniing instance
    instance_ID = response['Reservations'][0]['Instances'][0]['InstanceId']

    # Terminate the ec2 instnaces
    ec2_client.terminate_instances(InstanceIds=[instance_ID])

    print(f"Instance {instance_ID} is being terminated. ")

# Call the  function to termainte the EC2 instance
terminate_instance() 
