# basic test file

from datetime import datetime
import logging
from twitch import TwitchClient





def getvalue(d):
    for k, v in d.items():
        if isinstance(v, dict):
            getvalue(v)
        else:
            print("{} : {}".format(k, v))
