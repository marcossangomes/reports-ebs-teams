import boto3

# Function to write tags values in EBS tags (Tribe and Squad)
def update_tag_in_vol_id(tags, vol_id):

    ec2 = boto3.resource('ec2', region_name='us-east-1')
    volume = ec2.Volume(vol_id)

    tag = volume.create_tags(
        DryRun=False,
        Tags=[
            {
                'Key': 'Tribo',
                'Value': tags.get('Tribo')
            },
        ]
    )
    tag = volume.create_tags(
        Tags=[
            {
                'Key': 'Squad',
                'Value': tags.get('Squad')
            },
        ]
    )

    return 200;
