import os

import tweepy
from dotenv import load_dotenv


load_dotenv()


# 各認証情報を準備
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

twitter_user_id = os.getenv("TWITTER_USER_ID")

# API認証
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

twitter = tweepy.API(auth)
print(twitter_user_id)
result = twitter.user_timeline(id=twitter_user_id, count=1)

print(result)
