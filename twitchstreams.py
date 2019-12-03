# Christian Bull
# Gets twitch streams as defined by the users

from datetime import datetime
import logging
from twitch import TwitchClient
from secrets import client_id

# pulls in channel names from txt file
with open('streamers.txt', 'r') as f:
    streams = f.read().split('\n')

stream_keys = [
        'name',         # 8
        'id',           # 0  
        'stream_type',  # 4
        'viewers',      # 2
        'url',          # 4
        'game',         # 1
        'status',       # 5
        'created_at'    # 3
        ]

# sets some logging up
now = datetime.now().date()

logging.basicConfig(
    filename='./logs/log-{}.log'.format(now),
    filemode='w',
    format='%(asctime)s-%(levelname)s-%(message)s'    
)

logger = logging.getLogger()

# debug mode
logger.setLevel(logging.DEBUG)
logger.info('Logging started')


# creates twitch client, logs some stuff yo
def get_client():
    try:
        client = TwitchClient(client_id())
        logger.info("Twitch client connection successful")
        return client
    except Exception as e:
        logger.error("Twitch client connection unsuccessful", exc_info=True)


def get_ids(client):
    try:
        users = client.users.translate_usernames_to_ids(streams)
    except Exception as e:
        logger.error("Stream IDs unsuccesful", exc_info=True)

    degenerates = {}

    # get usernames and stream_ids
    for user in users:
        degenerates[user.name] = user.id

    return degenerates

def get_streams(client):
    logger.info("Getting stream info")
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
    logger.info("Finding live streams")

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
