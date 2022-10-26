from base64 import encode

from telnetlib import SE
import snscrape.modules.twitter as sntwitter 
import pandas as pd
from tw import Sentiment

# ------------text split--------------
def text_split(tweet):
    # precprcess tweet
    tweet_words = []
    for word in tweet.split(' '):
        if len(word.split('\n')) >1:
            for words in word.split('\n'):
                if words.startswith('http'):
                    words = "http"
                elif word.startswith('@') and len(word) > 1:
                    words = '@user'
                tweet_words.append(words)
        elif word.startswith('@') and len(word) > 1:       
            word = '@user'
        elif word.startswith('http'):
            word = "http"

        elif len(word.split('\n')) ==1:
            tweet_words.append(word)
    tweet_proc = " ".join(tweet_words)
    return tweet_proc
#-------------------speichern in CSV Datei----------------
def save(tweets,file_name):
    df = pd.DataFrame(tweets ,columns=['Date','User','Tweet','Sentiment','likeCount','retweetCount'])
    df.to_csv(file_name,sep='\t',header=False, mode='a')

query="(#EnergyTips) lang:en until:2022-11-25 since:2006-01-01"
tweets = []
posetive_tweets=[]
negative_tweets=[]
neutral_tweets=[]
limit =1000
inc=0

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets)==limit:
         break
    else :
        content_sentiment = Sentiment.sentiment_scores(tweet.content)    
        contenttext = str(text_split(tweet.content))
        if content_sentiment =='Positive':     
            posetive_tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment ,tweet.likeCount,tweet.retweetCount])
        elif content_sentiment =='Negative':
            negative_tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment,tweet.likeCount,tweet.retweetCount])
        elif content_sentiment =='Neutral':
            neutral_tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment,tweet.likeCount,tweet.retweetCount])
        
        tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment,tweet.likeCount,tweet.retweetCount])
        inc+=1
        print(inc)

#ganze tweets
save(tweets,'EnergyTips.csv')
#Positive tweets
save(posetive_tweets,'EnergyTips_posetive_tweets.csv')
#Negative tweets
save(negative_tweets,'EnergyTips_negative_tweets.csv')
#neutral tweets
save(neutral_tweets,'EnergyTips_neutral_tweets.csv')

