import random
import pandas as pd
import time

# Set up the initial condition.
number_of_tweet = 10000
num_of_users = 1000

# open the txt file to read each line
corpus = open('res/corpus.txt', encoding = "ISO-8859-1").readlines()

# generate random tweets by selecting the row of the file
text = []
ids = []
i = 0
while i < number_of_tweet:
    tweet = '\n'
    while tweet == '\n':
        tweet = random.choice(corpus)

        if len(tweet) > 100:
            tweet = tweet[:100]
    
    text.append(tweet)
    ids.append(random.randint(1, num_of_users))
    i+=1

# store the data into csv file
tweets = pd.DataFrame({'user_id':ids, 'tweet_text':text})
tweets.to_csv("tweets.csv")
