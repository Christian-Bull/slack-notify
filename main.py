"""
@Christian Bull
Created: 11/12/2019
Updated: 11/18/2019

This is a basic slack bot that posts custom notifications

"""

import time
import json
import requests
import twitchstreams # twitch wrapper
import secrets       # :wala:

# slack and twitch info
hook = secrets.bot_test()


# this takes json format and posts to channel in hook
def post_message(msg):
    data_json = json.dumps(msg)
    requests.post(hook, data=data_json)

test_data = {"text": "test 1 2 3 4"}

post_message(test_data)

"""
while True:
    print('test')
    info = twitchstreams.get_info(client)
    time.sleep(10)

    #
"""
# main
client = twitchstreams.get_client()

# check stream data

# if a stream is_created since last check, post to slack
# need to incorperate logging
