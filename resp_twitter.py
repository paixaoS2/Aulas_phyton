import tweepy
import time

api_key = 'pB8s9XXElBdBaxRGJa8X2f83x'
api_secret = 'YMVhLvecdgNwVfb992dzwVrG40fXGKTz3rhtV3cAsmW2QNJXeN'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABdnfgEAAAAAjWpf8hT%2FOTdU6h4wKAb5HaKbaFM%3Dil2CMGuOVjk8fuQ8teaLtEjsJ6eRCwGoB8NRypCKA6UlTXlDnH'
access_token = '821728943992700928-okHlkfN7kH4KzJHimc7lll8vjJi0LiC'
access_token_secret = 'gv567ywBXycFvQhlzdP1LGCZYqBKgZr1QwVOyyl5qAiUA'

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

menssage = 'Fortnite our la babagi?????!!!!!!'
client_id = client.get_me().data.id

start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

while True:
    response = client.get_users_mentions(client_id, since_id=start_id)
    
    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=menssage)
                start_id = tweet.id
            except Exception as error:
                print(error)
    time.sleep(5)           