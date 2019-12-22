# this code allows us to search Twitter for keyword(s) and collect the tweets on a .csv file
# it can also collect tweets within a certain timeframe
import tweepy
import csv
import time
import json

# use the Tweepy python library to access the Twitter API
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

#  this function takes out characters that can break import into Excel and replaces them with spaces
#  it also does the unicode bit
def getVal(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val.encode('utf-8')
        return clean

# sets up a file to write to
csvfile = open('streamed_tweets.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter='|')

query = '' #keyword goes here
max_tweets = 10000 #set a max number of tweets to collect

# since_id and max_id allow you to set a timeframe for tweet scraping if not collecting tweets live
# wait_on_rate_limit automatically waits for rate limits to replenish
# tweet_mode='extended' avoids tweets showing as truncated
for status in tweepy.Cursor(api.search, q=query, since_id=,
                            max_id=, wait_on_rate_limit=True,
                            tweet_mode='extended').items(max_tweets):
    try:
        tweet = dict(status._json)
        tweet_text = tweet['full_text']
        # write the values to .csv file
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
            tweet['user']['id']
            ])
    except Exception, err:
        print(err)
        pass
