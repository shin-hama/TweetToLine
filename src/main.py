from datetime import datetime, timezone, timedelta

from config import TWITTER_USER_ID
from get_tweet import get_tweet
from send_message import send_image, send_message

JST = timezone(timedelta(hours=9), "JST")


def main():
    """
    Get latest tweet and notify it by line bot
    """
    tweet = get_tweet(TWITTER_USER_ID)

    now = datetime.now(JST)

    if isinstance(tweet.created_at, datetime):
        delta = now - tweet.created_at
    else:
        # 日付がわからないときは判別不可能なので、何もしない
        return

    if delta.days > 1:
        # Tweet 更新なしとする
        return

    send_message(tweet.text)

    for media in tweet.extended_entities["media"]:
        send_image(media["media_url_https"])


if __name__ == "__main__":
    main()
