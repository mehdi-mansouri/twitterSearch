from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Sentiment:
    def sentiment_scores(sentence):
    
        # Create a SentimentIntensityAnalyzer object.
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_arr=[]
        # polarity_scores method of SentimentIntensityAnalyzer
        # object gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
        sentiment_dict = sid_obj.polarity_scores(sentence)
        
        #print("Overall sentiment dictionary is : ", sentiment_dict)
       # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
        sentiment_arr.append(sentiment_dict['neg']*100)
        #print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
        sentiment_arr.append(sentiment_dict['neu']*100)
       # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
        sentiment_arr.append(sentiment_dict['pos']*100)
    
        #print("Sentence Overall Rated As", end = " ")
    
        # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05 :
            result = "Positive"
        elif sentiment_dict['compound'] <= - 0.05 :
            result = "Negative" 
        else :
            result = "Neutral"
        print(result)
        return result
   