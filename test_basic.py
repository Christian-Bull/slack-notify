# basic test file

from twitch import TwitchClient

streams = [
    'odablock',
    'amenityrs'
]

client = TwitchClient('69e1k9ao573ly7f9f5invl44v2axxk')

def get_ids():
    users = client.users.translate_usernames_to_ids(streams)

    u = {}

    for user in users:
        u[user.name] = user.id

    return u

def get_streams():
    u = get_ids()

    live_streamers = {}

    for key, value in u.items():
        u, id = key, value

        live = client.streams.get_stream_by_user(id)

        live_streamers[u] = live

    return live_streamers

print(get_streams())