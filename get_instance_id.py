import boto3


# Retrieve the instance id through the volume id
def get_instance_id(vol_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    details = ec2.Volume(vol_id)
    return details.attachments[0].get('InstanceId')
