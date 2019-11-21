"""
@Christian Bull
Created: 11/12/2019
Updated: 11/19/2019

This is a basic slack bot that posts custom notifications

"""

import time
from datetime import datetime
from datetime import timedelta
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


# gets streams from twitchstreams
def get_streaminfo():
    streaminfo = twitchstreams.main()
    return streaminfo


# formats data into message
def send_message(stream_data):
    time_const = datetime.utcnow() - timedelta(minutes=5)

    for k, v in stream_data.items():
        if v[0] == 'offline':
            continue

        # if stream created time is in the last 5 min, post it yo
        elif v[3] > time_const:
            name = k
            stream_type = v[4]
            game = v[1]
            url = v[10]
            status = v[5]

            # formats message
            msg = "{} is now {}! Game: {}\n `{}`\n {}".format(name, stream_type, game, status, url)
            
            post_message({
               "text": msg
            })


# main
def main():
    data = get_streaminfo()
    send_message(data)


while True:
    main()
    time.sleep(300)


