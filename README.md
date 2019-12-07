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

`sudo docker build . -t slack-notify`

Run docker image:  

`sudo docker run -d slack-notify`

Note that the docker uses the base image of `python:3.7-alpine`  
<br>


## Deployment

I currently have this deployed on a k8s cluster. So I'll descibe how I set this up below. 

Note: I didn't create the cluster, I've only deployed stuff on it.

### Create Docker image and tag to registry:  

`sudo docker build .`

`sudo docker tag [image id] [registry:tag]`

For me this was :

`sudo docker tag 8922d588eec6 csbull55/slack-notify:initial`  
<br>

### Setup Kubernetes config:

I hosted this on a private registry so I had to create a secret for use in k8s. I'm not going to cover this here as there's documentation on kubernetes site already on it.

```
apiVersion: v1
kind: Pod
metadata:
  name: slack-notify
spec:
  containers:
    - name: slack-notify
      image: csbull55/slack-notify:initial
      env:
        - name: PYTHONUNBUFFERED
          value: "0"
  imagePullSecrets:
    - name: slacknotifycred
  restartPolicy: OnFailure
  ```

This creates a pod named 'slack-notify' based on our docker image. Accessing the private registry using the secret I created in k8s.

`kubectl apply -f deploy.yaml`

Should return:

```
pod/slack-notify created
```

Alright lets see if it's running

`kubectl get pod slack-notify`

```
NAME           READY   STATUS    RESTARTS   AGE
slack-notify   1/1     Running   0          49m
```

<br>
Let's get some logs

`kubectl logs slack-notify`

```
2019-12-06 23:46:44,503-INFO-Logging started
2019-12-06 23:46:44,503-INFO-Initiating get_stream()
2019-12-06 23:46:44,503-INFO-Twitch client connection successful
2019-12-06 23:46:44,503-INFO-Finding live streams
2019-12-06 23:46:44,503-INFO-Getting stream info
```

When you mess up the initial deployment (not speaking from experience), k8s makes it super easy to clean up your mess.

`kubectl delete pod [name]`