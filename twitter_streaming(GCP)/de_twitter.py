import json,tweepy
from google.cloud import pubsub_v1
from google.oauth2 import service_account

key_path = 'twitterstreaming-335700-dfa6120bb104.json'
# t_key =
# t_s_key =
# access_token =
# access_s_token =

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = client.topic_path('twitterstreaming-335700','tweets')

class SimpleStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
        tweet = json.dumps({'id': status.id, 'created_at': status.created_at , 'text': status.text} , default=str)
        client.publish(topic_path , data = tweet.encode('utf-8'))
    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return false


stream_listener = SimpleStreamListener()
auth = tweepy.OAuthHandler(t_key, t_s_key)
auth.set_access_token(access_token, access_s_token)

twitterStream = tweepy.Stream(auth, stream_listener)
twitterStream.filter(track=['football'])

