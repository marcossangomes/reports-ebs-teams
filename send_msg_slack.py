import os
import slack

# Function to send report file on Slack channel..
def send_msg_slack(count_is, count_av, count_vt):
    slack_token = os.environ['SLACK_TOKEN']
    client = slack.WebClient(token=slack_token)
    env = os.environ['ENV']

    client.chat_postMessage(
        channel="channel-name",
        text="Enviroment: " + env + "\n" +
             "Tagged Volumes: " + str(count_vt) +
            '\nVolumes with status "available": ' + str(count_av) +
             "\nUntagged Instances: " + str(count_is)
    )

    client.files_upload(
        channels="channel-name",
        file="instances.txt",
        title="Upload report"
    )