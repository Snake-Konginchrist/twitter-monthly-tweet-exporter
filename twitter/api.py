from datetime import datetime

import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


# 初始化API
def initialize_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


# 获取推文，包含按日期筛选的逻辑
def get_tweets(username, year, month):
    api = initialize_api()
    start_date = datetime(int(year), int(month), 1)
    end_date = datetime(int(year), int(month) + 1, 1) if int(month) < 12 else datetime(int(year) + 1, 1, 1)

    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items():
        if start_date <= tweet.created_at < end_date:
            tweets.append(tweet)
    return tweets
