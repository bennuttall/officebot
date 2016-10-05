# Slack Office Robot

A Raspberry Pi powered office robot controlled by Slack commands

## Hardware

- [Raspberry Pi](https://www.raspberrypi.org/products/) (any model - ideally with WiFi, or use a WiFi dongle)
- Motor controller board (e.g. [CamJam kit 3](http://camjam.me/?page_id=1035))
- 2 motors
- USB battery pack

## Software

- [GPIO Zero](https://gpiozero.readthedocs.io)
- [Python Slack Client](https://python-slackclient.readthedocs.io)

To install:

```bash
sudo apt-get update
sudo apt-get install python3-gpiozero python3-pip -y
sudo pip3 install slackclient
```

## Setup 

You will need to register an app at [api.slack.com/apps](https://api.slack.com/apps) and generate an access token.

You also need to find the channel ID of the channel you wish to listen to. To do this, open a Python shell and type:

```python
from slackclient import SlackClient
slack = SlackClient("YOUR TOKEN")
slack.server.channels.find("CHANNEL")
```

You will see a response including the channel ID.

Then enter your token and channel ID into the variables in `secret.py` and be careful to keep this file secret (don't accidentally push it to GitHub).

## Modifying

To use another motor controller board, swap [`CamJamKitRobot`](http://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#camjam-3-kit-robot) to [`Robot`](http://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#robot) and use the appropriate motor pin numbers.
