import tweepy
import csv
import time
import json

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status

def getVal(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val.encode('utf-8')
        return clean

# setup a file to write to
csvfile = open('WAB_final_tweepy.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter='|')

query = '' #enter keywords here
max_tweets = 10000

for status in tweepy.Cursor(api.search, q=query, since_id=,
                            max_id=, wait_on_rate_limit=True,
                            tweet_mode='extended').items(max_tweets):
#enter since and max ids
    try:
        tweet = dict(status._json)
        tweet_text = tweet['full_text']
        # write the values to file
        print(tweet_text)
        csvwriter.writerow([
            tweet['created_at'],
            getVal(tweet['user']['screen_name']),
            getVal(tweet_text),
            getVal(tweet['user']['location']),
            tweet['user']['geo_enabled'],
            tweet['place'],
            tweet['lang'],
            tweet['retweet_count'],
            tweet['source'],
            tweet['user']['verified'],
            tweet['user']['statuses_count'],
            tweet['user']['followers_count'],
            tweet['user']['friends_count'],
            tweet['user']['created_at'],
            tweet['user']['id'],
            tweet['user']['following']
            ])
    except Exception, err:
        print(err)
        pass
