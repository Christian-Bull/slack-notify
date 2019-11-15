# Christian Bull
# Gets twitch streams as defined by the users

from datetime import datetime
import logging
from twitch import TwitchClient

# define channel names to check here, this is a stateless app
# otherwise I'd define these externally somehow
streams = [
        'odablock',
        'thekraut',
        'amenityrs'
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
    logger.info('This bot is baaaad')
    logger.info('Logging started')

    return logger
    
# creates twitch client, logs some stuff yo
def get_client(logger):
    try:
        client = TwitchClient('69e1k9ao573ly7f9f5invl44v2axxk')
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

    live_streamers = {}

    # takes id and creates dictionary of live streamers and associated info
    for key, value in u.items():
        u, id = key, value

        live = client.streams.get_stream_by_user(id)

        live_streamers[u] = live

    return live_streamers


# gets info about live users
def get_info(client):
    live_degens = get_streams(client)

    # recursive func, goes through tree of dictionary to get values :wala:
    def getvalue(d):
        for k, v in d.items():
            if isinstance(v, dict):
                getvalue(v)
            else:
                print("{} : {}".format(k, v))

    return getvalue(live_degens)

# main still testing
def main():
    logger = log()              # creates logger
    client = get_client(logger) # creates client
    stuff = get_info(client)    # gets info
    
    print(stuff)


main()
# wanted to hit 100 lines lmao :wala:
