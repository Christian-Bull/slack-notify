# Christian Bull
# Gets twitch streams as defined by the users

from twitch import TwitchClient

streams = [
    'odablock',
    'thekraut',
    'amenityrs'
]

client = TwitchClient('69e1k9ao573ly7f9f5invl44v2axxk')


def get_ids():
    users = client.users.translate_usernames_to_ids(streams)

    degenerates = {}

    # get usernames and stream_ids
    for user in users:
        degenerates[user.name] = user.id

    return degenerates

def get_streams():
    u = get_ids()

    live_streamers = {}

    # takes id and creates dictionary of live streamers and associated info
    for key, value in u.items():
        u, id = key, value

        live = client.streams.get_stream_by_user(id)

        live_streamers[u] = live

    return live_streamers


# gets info about live users
def get_info():
    live_degens = get_streams()

    def getvalue(d):
        for k, v in d.items():
            if isinstance(v, dict):
                getvalue(v)
            else:
                print("{} : {}".format(k, v))

    return getvalue(live_degens)


def main():
    get_info()


main()