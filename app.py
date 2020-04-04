from get_instance_id import get_instance_id
from check_tag_instance_id import check_tag_instance_id
from update_tag_in_vol_id import update_tag_in_vol_id
from send_msg_slack import send_msg_slack
from list_all_vol_id import list_all_vol_id
from send_msg_gchat import send_msg_gchat


all_vol = list_all_vol_id()

# These counters are to maintain the value when sending the report to Slack
count_vt = 0  # contado volume tageado
count_is = 0  # contador instancia sem tag
count_av = 0  # contador volume com status available

arquivo = open('instances.txt', 'w')


for vol in all_vol:
    try:
        instance_id = get_instance_id(vol)
        tribe = check_tag_instance_id(instance_id)['Tribe']
        squad = check_tag_instance_id(instance_id)['Squad']

        if tribe != '' and squad != '':
            # Get the value in tag TEAM
            tags = check_tag_instance_id(get_instance_id(vol))

            # Update the value in tag TEAM on EBS(Elastic Block Storage - AWS)
            update_tag_in_vol_id(tags, vol)
            print('Tagged Volum ', vol)
            arquivo.write('Tagged Volum ' + vol + '\n')
            count_vt = count_vt + 1
        else:
            print("Untagged Instances ", (get_instance_id(vol)))
            arquivo.write("Untagged Instances " + (get_instance_id(vol)) + '\n')
            count_is = count_is + 1
    # and the exception to deal with what is different from the EBS 'In use' status
    except Exception as err:
        print('Untagged Volume ', vol, ' the volume status is in "available"')
        arquivo.write('Untagged Volume '+ vol + 'the volume status is in "available"\n')
        count_av = count_av + 1

# Write mapped values in the file;
arquivo.write('Tagged Volumes ' + str(count_vt))
arquivo.write('\n')
arquivo.write('Untagged Instances ' + str(count_is))
arquivo.write('\n')
arquivo.write('Volumes with status "available" ' + str(count_av))
arquivo.close()

# function to send report file 'instances.txt' and mapped values;
send_msg_gchat(count_is, count_av, count_vt)