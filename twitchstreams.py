# Christian Bull
# Gets twitch streams as defined by the users

from datetime import datetime
import logging
from twitch import TwitchClient
from secrets import client_id

# define channel names to check here, this is a stateless app
# otherwise I'd define these externally somehow
streams = [
        'odablock',
        'thekraut',
        'amenityrs'
        ]

stream_keys = [
        'name',         # 0
        'id',           # 1  
        'stream_type'   # 2
        'viewers',      # 3
        'url',          # 4
        'game',         # 5
        'status'        # 6
        'created_at'    # 7
        ]


# sets some logging up
now = datetime.now().date()

logging.basicConfig(
    filename='./logs/log-{}.log'.format(now),
    filemode='w',
    format='%(asctime)s %(message)s'    
)

logger = logging.getLogger()

# debug mode
logger.setLevel(logging.DEBUG)
logger.info('This bot is baaaad')
logger.info('Logging started')


# creates twitch client, logs some stuff yo
def get_client():
    try:
        client = TwitchClient(client_id())
        logger.info("Twitch client connection successful")
        return client
    except:
        logger.error("Twitch client connection unsuccessful ERRORLMAO")


def get_ids(client):
    try:
        users = client.users.translate_usernames_to_ids(streams)
    except:
        print('unable to get ids for specified users')

    degenerates = {}

    # get usernames and stream_ids
    for user in users:
        degenerates[user.name] = user.id

    return degenerates

def get_streams(client):
    u = get_ids(client)

    streamers = {}

    # takes id and creates dictionary of live streamers and associated info
    for key, value in u.items():
        u, id = key, value

        live = client.streams.get_stream_by_user(id)

        streamers[u] = live

    return streamers


# gets info about live users
def get_info(client):

    # creates buckets
    streamer_info = get_streams(client)
    streamer_formatted = {}
    logger.info(streamer_info)

    # finds live streamers
    for k, v in streamer_info.items():
        
        # if there's no data, stream is offline
        if v == None:
            streamer_formatted[k] = ['offline']

        else:
            items = []

            # sets up recursive function to go through dictionary and nests
            # if a key is in the stream_keys, it adds it to the data returned list
            def getvalue(d):
                for k, v in d.items():
                    if isinstance(v, dict):
                        getvalue(v)
                    else:
                        if k in stream_keys:
                            items.append(v)

            getvalue(v)

            streamer_formatted[k] = items
 
    # logs streams
    logger.info(streamer_formatted)

    return streamer_formatted


# main still testing
def main():
    client = get_client() # creates client
    data = get_info(client)    # gets info
    
    return data
