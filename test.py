tweet ='hallo mehdi mansouri #GasTips\nhttps://t.co/qTXR7wECcl'
arr = tweet.split('\n')
print(len(arr))
print(arr)
tweet_words =[]
for word in tweet.split(' '):
    if len(word.split('\n')) >1:
        for words in word.split('\n'):
            if words.startswith('http'):
                words = "http"
            elif word.startswith('@') and len(word) > 1:
                words = '@user'
            print(words)
            tweet_words.append(words)
    elif word.startswith('@') and len(word) > 1:
        print(word)
        word = '@user'
    elif word.startswith('http'):
        print(word)
        word = "http"

    elif len(word.split('\n')) ==1:
        tweet_words.append(word)
    print(tweet_words)
    tweet_proc = " ".join(tweet_words)