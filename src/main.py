import os

from dotenv import load_dotenv
from linebot import LineBotApi
import tweepy
from linebot.models import TextSendMessage

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
result = twitter.user_timeline(id=twitter_user_id, count=1)

tweet_text = result[0].text

ACCESS_TOKEN = os.getenv("LINE_BOT_ACCESS_TOKEN")

line_bot_api = LineBotApi(ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text=tweet_text))
