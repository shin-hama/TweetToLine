from datetime import datetime, timezone, timedelta
import os

from dotenv import load_dotenv
from linebot import LineBotApi
import tweepy
from tweepy.models import Status
from linebot.models import ImageSendMessage, TextSendMessage


load_dotenv()

# 各認証情報を準備
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

twitter_user_id = os.getenv("TWITTER_USER_ID")

# API認証
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

twitter = tweepy.API(auth)
result: list[Status] = twitter.user_timeline(id=twitter_user_id, count=1)

# 最新のツイートを取得
tweet = result[0]

JST = timezone(timedelta(hours=9), "JST")
now = datetime.now(JST)

if isinstance(tweet.created_at, datetime) is False:
    # 日付がわからないときは判別不可能なので、何もしない
    exit()

delta: timedelta = now - tweet.created_at
if delta.days > 1:
    # Tweet がないときは更新しないこととする
    exit()

line_access_token = os.getenv("LINE_BOT_ACCESS_TOKEN")

line = LineBotApi(line_access_token)
line.broadcast(TextSendMessage(text=tweet.text))

for media in tweet.extended_entities["media"]:
    line.broadcast(
        ImageSendMessage(
            original_content_url=media["media_url_https"],
            preview_image_url=media["media_url_https"],
        )
    )
