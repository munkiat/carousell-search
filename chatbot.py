from slackclient import SlackClient
from configurations import SLACK_TOKEN, SLACK_CHANNEL

slack_notifier = SlackClient(SLACK_TOKEN)

def post_message(msg):
    slack_notifier.api_call(
        "chat.postMessage",
        channel=SLACK_CHANNEL,
        text=msg,
        username = 'CarousellBot',
        icon_emoji=':robot_face:'
    )
