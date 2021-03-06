import os, tweepy, pandas
import twitter
import datetime


consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

api = twitter.Api(consumer_key = consumer, consumer_secret = c_secret, 
                    access_token_key = token, access_token_secret = at_secret)

mylist = None
with open('editedTweet.json') as json_file:
    mylist = json.load(json_file)


start = datetime.strptime('your start time', '%b %d %H:%M:%S %z %Y')
end = datetime.strptime('your end time', '%b %d %H:%M:%S %z %Y')

myTweet = []

for item in mylist:
    tweet_time = datetime.strptime(item["tweet"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
    if (tweet_time >= start and tweet_time <= end):
        myTweet.append(item["tweet"]["id_str"])

print(myTweet)

