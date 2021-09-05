import os
import json
import slack


def get_bot_conf():
    """Retrives bot config data such as token, channels and messages"""
    conf_path = os.path.abspath("examples.json")
    with open(conf_path, "r") as conf_file:
        conf = json.loads(conf_file.read())
    return conf.get("bot_token"), conf.get("channels")


token, messages = get_bot_conf()
client = slack.WebClient(token=token)

for message in messages:
    channel = "#" + message.get("channel")
    sent_text = message.get("text")
    client.chat_postMessage(channel=channel, text=sent_text)
    print(f'Message "{sent_text} is sent successfully to channel "{channel}"')