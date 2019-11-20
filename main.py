"""
@Christian Bull
Created: 11/12/2019
Updated: 11/19/2019

This is a basic slack bot that posts custom notifications

"""

import time
import json
import requests
# import twitchstreams # twitch wrapper
import secrets       # :wala:

# slack and twitch info
hook = secrets.bot_test()


# this takes json format and posts to channel in hook
def post_message(msg):
    data_json = json.dumps(msg)
    requests.post(hook, data=data_json)

def get_streaminfo():
    
# main

# client = twitchstreams.get_client()

# check stream data

# if a stream is_created since last check, post to slack
# need to incorperate logging
