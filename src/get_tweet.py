import os

import tweepy
from tweepy.models import Status

from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
)

# API認証
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)


def get_tweet(user_id: str):
    """
    指定した User の最新ツイートを取得する

    parameter
    ---------
    user_id: user id to get tweet
    """
    result: list[Status] = twitter.user_timeline(user_id=user_id, count=1)

    # 最新のツイートを取得
    return result[0]
