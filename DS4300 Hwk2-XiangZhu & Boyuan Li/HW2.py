# work together by Xiang Zhu & Boyuan Li
import pandas as pd
import time
import random
from abc import ABC, abstractmethod

# In order to make the code well-structured, the twitter API
# should define an interface that include operations
# for reading and writing to the backend database.
# In python, we can use abstract class to achieve interface function.
class TwitterAPI(ABC):

    def __init__(self, api):
        self.api = api
        super().__init__()
    
    @abstractmethod
    def add_followers(self):
        pass

    @abstractmethod
    def get_followers(self, user_id):
        pass
    
    @abstractmethod
    def get_followees(self, user_id):
        pass

    @abstractmethod
    def post_tweets(self, strategy):
        pass

    @abstractmethod
    def get_timeline(self, user_id, strategy):
        pass

    @abstractmethod
    def clear_db(self):
        pass

# RedisAPI inherits from the TwitterAPI
class RedisAPI(TwitterAPI):
    
    def __init__(self,api):
        super().__init__(api)

    # add followers that the user was followed.
    def add_followers(self):
        follows = pd.read_csv('follows.csv')
        # 10000 users
        for i in range(1, 10000):
            # user_id.
            key1 = "followers:" + str(i)
            # the list of ids who follows the user.
            vals1 = follows.loc[follows['follows_id'] == i]['user_id'].tolist()
            # Add the specified members to the set stored at key.
            for ids in vals1:
                self.api.sadd(key1, ids)

            key2 = "followee:" + str(i)
            # the list of ids who the user follows.
            vals2 = follows.loc[follows['user_id'] == i]['follows_id'].tolist()
            # Add the specified members to the set stored at key.
            for ids in vals2:
                self.api.sadd(key2, ids)

    # who is following user_id
    def get_followers(self, user_id):
        key = "followers:" + str(user_id)
        # Returns all the members of the set value stored at key.
        followers = list(self.api.smembers(key))
        # list of ids.
        return ([x.decode() for x in followers])

    # who is user_id following
    def get_followees(self, user_id):
        key = "followee:" + str(user_id)
        # Returns all the members of the set value stored at key.
        followees = list(self.api.smembers(key))
        # list of ids.
        return ([x.decode() for x in followees])

    # Reads pre-generated tweets from the file and loads them into Redis database
    def post_tweets(self, strategy):
        tweets = pd.read_csv("tweets.csv")

        start_time = time.time()
        
        for i in range(len(tweets)):

            tweet_text = tweets['tweet_text'][i]
            user_id = tweets['user_id'][i]
            
            # ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # TWEETS [tweet_id, user_id, tweet_ts, tweet_text]

            # set tweet id with tweet text
            next_tweet_id = self.api.incr('nextTweetID')
            self.api.set(next_tweet_id, tweet_text)

            # Strategy 1: When you post a tweet, it is a simple addition
            # of a key and a value.
            if not strategy:
                key = "tweet:" + str(user_id)
                self.api.lpush(key, next_tweet_id)
            # Strategy 2: As you post each tweet, you copy the tweet
            # to the user’s home timeline automatically. 
            else:
                followers = self.get_followers(user_id)
                for ids in followers:
                    key = "timeline:" + str(ids)
                    self.api.lpush(key, next_tweet_id)

        end_time = time.time()
        running_time = end_time - start_time
        avg_tweets_per_second = 1000000 / running_time
        
        print('How many tweets can be posted per second:',
              strategy, avg_tweets_per_second)

    # get the user’s home timeline.
    def get_timeline(self, user_id, strategy):

        start_time = time.time()

        # Strategy 1: Look up the tweets of each of your followers,
        # constructing the home timeline on the fly on demand
        if not strategy:
            tweet_ids = []
            followees = self.get_followees(user_id)
            followees = ["tweet:" + s for s in followees]
            tweets = []
            for key in followees:
                ids = self.api.lrange(key, 0 ,-1)
                ids = [x.decode() for x in ids]
                tweet_ids += ids
            tweet_ids.sort(reverse = True)
            for tweet_id in tweet_ids:
                tweets.append(self.api.get(tweet_id))
            
        else:
        # Strategy 2: the timeline is now ready and waiting,
        # getTimeline should be a much faster operation
            key = "timeline:" + str(user_id)
            tweet_ids = self.api.lrange(key, 0, 9)
            tweet_ids = [x.decode() for x in tweet_ids]
            tweets = []
            for tweet_id in tweet_ids:
                tweets.append(self.api.get(tweet_id))
        
        end_time = time.time()
        running_time = end_time - start_time
        print('How many home timeline can be refreshed per second:',
              strategy, 1/running_time)
            
    # Delete all the keys of all the existing databases
    def clear_db(self):
        self.api.flushall()
