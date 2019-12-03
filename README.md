# Slack-Notify

This is a basic slack notification bot using Python. This specific use case is to notify a slack channel if a user goes live on twitch.

### Setup

Clone repository:  
`$ git clone https://github.com/Christian-Bull/slack-notify.git`  


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
<br>

In `./streamers.txt`, set which channel names you'd like the bot to ping. Put each channel name on a separate line.
```
streamer1
streamer2
etc.
```

<br>

Build docker image:  
`$ sudo docker build . -t slack-notify`

Run docker image:  
`$ sudo docker run -d slack-notify`

Note that the docker uses the base image of `python:3.7-alpine`  
<br>

## Notes

This is currently set to run every 5 mins as definied in `./main.py`. A better setup would be to setup would be to run it as a job every x mins when you deploy it. Either by cronjobs or k8s equivelant.

Replace:
```
while True:
    main()
    time.sleep(300)
```
With:
```
main()
```
