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
        'name',
        'id',
        'stream_type',
        'viewers',
        'url',
        'game',
        'status',
        'created_at'
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
        print('lol')

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
        if v == None:
            streamer_formatted[k] = 'Offline'
        else:
            displayname = k
            def getvalue(d):
                for k, v in d.items():
                    if k in stream_keys:
                        streamer_formatted[displayname]
                    else:
                        if isinstance(v, dict):
                            getvalue(v)


            getvalue(v)
    
    print(streamer_formatted)

    # # recursive func, goes through tree of dictionary to get values :wala:
    # def getvalue(d):
    #     for k, v in d.items():
    #         if k in stream_keys:
    #             logger.info('{} : {}'.format(k, v))

    #         if isinstance(v, dict):
    #             #logger.info('dict {}'.format(k))
    #             getvalue(v)

    #         else:
    #             if k in stream_keys:
    #                 # streamer_formatted[k] = v
    #                 #print(k, v)
    #                 h = 10

    # getvalue(streamer_info)

    logger.info("LIVE STREAMS ********************")  
    logger.info(streamer_formatted)

    return streamer_formatted

# main still testing
def main():
    client = get_client() # creates client
    stuff = get_info(client)    # gets info
    
    print(stuff)

main()
