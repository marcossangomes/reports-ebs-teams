import boto3


# Function to get values from Tags (Tribe and Squad) 
def check_tag_instance_id(inst_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.Instance(inst_id)

    Keys = {"Tribe": "", "Squad": ""}

    for tags in instance.tag:
        if tags.get('Key', 0) == 'Tribe' and tags.get('Value', 0) != '':
            Keys.update({"Tribe": tags['Value']})
        if tags.get('Key', 0) == 'Squad' and tags.get('Value', 0) != '':
            Keys.update({"Squad": tags['Value']})

    return Keys