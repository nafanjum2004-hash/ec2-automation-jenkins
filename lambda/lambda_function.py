import boto3
import os
import json
import time

def lambda_handler(event, context):

    region = os.environ["REGION_NAME"]
    ami_id = os.environ["AMI_ID"]
    instance_type = os.environ["INSTANCE_TYPE"]
    key_name = os.environ["KEY_NAME"]

    ec2 = boto3.client("ec2", region_name=region)

    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response["Instances"][0]["InstanceId"]

    time.sleep(15)

    instance_details = ec2.describe_instances(
        InstanceIds=[instance_id]
    )

    instance = instance_details["Reservations"][0]["Instances"][0]

    print("-----------")
    print(f"Instance ID: {instance['InstanceId']}")
    print(f"State: {instance['State']['Name']}")
    print(f"Instance Type: {instance['InstanceType']}")
    print(f"Region: {region}")
    print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
    print(f"Private IP: {instance.get('PrivateIpAddress', 'N/A')}")
    print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")

    return {
        "statusCode": 200,
        "body": "EC2 Instance Created Successfully"
    }