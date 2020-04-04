import boto3


# Function to return a list with all volumes ids
def list_all_vol_id():
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    volumes = ec2.volumes.all()
    all_vol_id = []
    for volume in volumes:
        all_vol_id.append(volume.id)

    return all_vol_id;