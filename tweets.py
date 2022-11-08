from base64 import encode
from telnetlib import SE
import snscrape.modules.twitter as sntwitter 
import pandas as pd
import numpy as np
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
                elif words.startswith('#'):
                   
                    words = ""
                elif word.startswith('@') and len(word) > 1:
                    words = '@user'
                tweet_words.append(words)
        elif word.startswith('@') and len(word) > 1:       
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        elif word.startswith('\\u'):
            word = ""
        elif word.startswith('#'):
            
            word = ""
        elif len(word.split('\n')) ==1:
            tweet_words.append(word)
    tweet_proc = " ".join(tweet_words)
    return tweet_proc
#-------------------speichern in CSV Datei----------------
def save(tweets,file_name):
    data_array =np.array(tweets)
    df=pd.DataFrame(data_array,columns=['tweet','likes' ,'retweet', 'sentiment'])
    df.to_json(file_name, orient='records')

query="(#energytips) lang:en until:2022-11-03 since:2006-01-01"
tweets = []
posetive_tweets=[]
negative_tweets=[]
neutral_tweets=[]
limit =100000
inc=0

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets)==limit:
         break
    else :
        content_sentiment = Sentiment.sentiment_scores(tweet.content)    
        contenttext = str(text_split(tweet.content))
        
        if content_sentiment =='Positive':     
            #posetive_tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment ,tweet.likeCount,tweet.retweetCount])
            posetive_tweets.append([contenttext ,tweet.likeCount ,tweet.retweetCount , content_sentiment])
            
        elif content_sentiment =='Negative':
            #negative_tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment,tweet.likeCount,tweet.retweetCount])
            negative_tweets.append([contenttext ,tweet.likeCount ,tweet.retweetCount , content_sentiment])
        elif content_sentiment =='Neutral':
            #neutral_tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment,tweet.likeCount,tweet.retweetCount])
            neutral_tweets.append([contenttext ,tweet.likeCount ,tweet.retweetCount , content_sentiment])
        
        #tweets.append([tweet.date, tweet.user.username,contenttext,content_sentiment,tweet.likeCount,tweet.retweetCount])
        tweets.append([contenttext ,tweet.likeCount ,tweet.retweetCount , content_sentiment])
        inc+=1
        print(inc)
        #print(contenttext)

#ganze tweets
#df=pd.DataFrame(tweets,columns=['tweet'])
#print(tweets)
save(tweets,'EnergyTips1.json')
#Positive tweets
save(posetive_tweets,'EnergyTips1_posetive_tweets.json')
#Negative tweets
save(negative_tweets,'EnergyTips1_negative_tweets.json')
#neutral tweets
save(neutral_tweets,'EnergyTips1_neutral_tweets.json')

