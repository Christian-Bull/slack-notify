"""
@Christian Bull
Created: 11/12/2019
Updated: 11/12/2019

This is a basic slack bot that posts custom notifications

"""

import time
import twitchstreams

# slack config


# twitch config
client = twitchstreams.get_client()


# main

while True:
    time.sleep(10)
    print('test')
    info = twitchstreams.get_info(client)
    print(info)