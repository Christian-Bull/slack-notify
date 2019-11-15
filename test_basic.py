# basic test file

from datetime import datetime
import logging
from twitch import TwitchClient


streams = [
    'odablock',
    'amenityrs',
    'lolnoneasdf'
]


# initiate logging
def log():
    now = datetime.now().date()

    logging.basicConfig(
        filename='log-{}.log'.format(now),
        filemode='w',
        format='%(asctime)s %(message)s'
        )

    logger = logging.getLogger()

    # debug mode
    logger.setLevel(logging.DEBUG)


# tries to get the twitch client initiated
def get_client():
    try:
        client = TwitchClient('69e1k9ao573ly7f9f5invl44v2axxk')
        logger.info('Client connection successful')
        return client
    except:
        logger.error('Client connection failure')


# gets channel ids off channel names provided
def get_ids():
    try:
        users = client.users.translate_usernames_to_ids(streams)
    except:
        print('lol')

    u = {}  

    for user in users:
        u[user.name] = user.id

    return u
    

# gets stream info for channel IDs
def get_streams():
    u = get_ids()

    live_streamers = {}

    for key, value in u.items():
        u, id = key, value

        live = client.streams.get_stream_by_user(id)

        live_streamers[u] = live

    return live_streamers

def main():
    log()

    
