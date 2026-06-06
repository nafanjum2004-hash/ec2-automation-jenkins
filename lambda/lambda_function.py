import boto3
import os
import json

def lambda_handler(event, context):

    region = os.environ["AWS_REGION"]
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

    instance_details = ec2.describe_instances(
        InstanceIds=[instance_id]
    )

    instance = instance_details["Reservations"][0]["Instances"][0]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "InstanceId": instance["InstanceId"],
            "State": instance["State"]["Name"]
        })
    }