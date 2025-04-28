Read full post
import json
import boto3

ec2list = []

def lambda_handler(event, context):

    # Get list of regions
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions().get('Regions',[] )

    # Iterate over regions
    for region in regions:

        print ("* Checking region  --   %s " % region['RegionName'])
        reg=region['RegionName']

        client = boto3.client('ec2', region_name=reg)
        response = client.describe_instances()

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                print ("  ---- Instance %s in %s" % (instance['InstanceId'], region['RegionName']))
                ec2list.append(instance['InstanceId'])

    return {
        "statusCode": 200,
        "body": ec2list
    }   
