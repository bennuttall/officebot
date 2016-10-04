from slackclient import SlackClient
from gpiozero import CamJamKitRobot
from secret import token, channel
from time import sleep

def event_filter(event):
    return 'channel' in event and event['channel'] == channel and 'text' in event

def process_instruction(instruction):
    if instruction in instructions:
        instructions[instruction]()
        print(event['text'])

slack = SlackClient(token)
robot = CamJamKitRobot()

if not slack.rtm_connect():
    raise Exception("Could not connect to Slack")

instructions = {
    'f': robot.forward,
    'b': robot.backward,
    'l': robot.left,
    'r': robot.right,
    's': robot.stop,
}

print("Ready...")
while True:
    events = slack.rtm_read()
    for event in filter(event_filter, events):
        process_instruction(event['text'])
    sleep(1)
