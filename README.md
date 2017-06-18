# carousell-search

Getting near real-time notifications on Carousell.

## Installing

`pip3 install requirements.txt`

## Configuring

Configure `myconfigurations.py` with 
- your Slack token from https://api.slack.com/tokens
- your Slack channel
- search queries in `ITEMS`

Ensure that your Slack app has the correct permissions to post in channel

## Running

`python3 main.py`
