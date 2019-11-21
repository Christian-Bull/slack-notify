# Slack-Notify

This is a basic slack notification bot using Python. I know this has been done over a _thousand_ times, but trust this one will be the best! (not even close)

This specific use case is to notify a slack channel if a user goes live on twitch.

The only catch of this app is that it's stateless. Meaning it doesn't store any data, and all references must be made in memory. Which made the code a little more _spicy_ than normal. Basically what I'm saying is that when you notice bad code, this is my excuse.

### Setup

Clone repository:  
`$ git clone https://github.com/Christian-Bull/slack-notify.git`  
`$ pip install -r requirements.txt`


Setup `./secrets.py`

```
# secrets file

def client_id():
    client_id = <twitch_client_id>

    return client_id

def bot_test():
    hookcity = <slack_webhook>
    return hookcity
```
