"""
@Christian Bull
Created: 11/12/2019
Updated: 11/19/2019

This is a basic slack bot that posts custom notifications

"""

import sys
import time
import logging
from datetime import datetime
from datetime import timedelta
import json
import requests
import twitchstreams # twitch wrapper
import secrets       # :wala:

# slack and twitch info
hook = secrets.bot_test()

# logging
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s-%(levelname)s-%(message)s'    
)

logger = logging.getLogger()

# debug mode
logger.setLevel(logging.DEBUG)
logger.info('Logging started')

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
            logger.info("{} is offline".format(k))
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
            
            logger.info("Message Sent for {}".format(k))
        
        else:
            logger.info("{0} went online at {1}".format(k, v[3]))


# main
def main():
    logger.info("Initiating get_stream()")
    data = get_streaminfo()
    send_message(data)
    logger.info("Finished main")

while True:
    main()
    time.sleep(300)
