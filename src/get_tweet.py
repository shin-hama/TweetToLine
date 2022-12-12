from datetime import datetime, timedelta, timezone
from typing import Iterator
import tweepy
from tweepy.models import Status

from .config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
)

# API認証
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)

JST = timezone(timedelta(hours=9), "JST")


def get_tweets_of_the_day(user_id: str, count: int = 5) -> Iterator[Status]:
    """
    指定した User の本日投稿したツイートを取得する

    parameter
    ---------
    user_id: user id to get tweet
    """
    result: list[Status] = twitter.user_timeline(user_id=user_id, count=count)

    # 本日のツイートのみでフィルター
    return reversed(list(filter(is_today, result)))


def is_today(tweet: Status) -> bool:
    if isinstance(tweet.created_at, datetime):
        now = datetime.now(JST)
        tweeted_at = tweet.created_at.astimezone(JST)
        delta = now - tweeted_at

        if delta.days > 1:
            return False
        else:
            # timedelta が 24 時間以内で、日付が同じなら本日のデータとする
            return tweeted_at.day == now.day
    else:
        # 日付がわからないときは判別不可能なので、何もしない
        return False
