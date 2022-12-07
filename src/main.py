from datetime import datetime, timezone, timedelta
import logging

from config import TWITTER_USER_ID
from get_tweet import get_tweet
from send_message import send_image, send_message

JST = timezone(timedelta(hours=9), "JST")

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


def main():
    """
    Get latest tweet and notify it by line bot
    """
    try:
        tweet = get_tweet(TWITTER_USER_ID)
    except Exception as ex:
        logger.error(ex)
        return

    logger.debug("Found tweet")
    logger.debug("username: %s", tweet.user.name)
    logger.debug("body: %s", tweet.text)

    if isinstance(tweet.created_at, datetime):
        now = datetime.now(JST)
        delta = now - tweet.created_at
    else:
        logger.warning("Unsupported format: tweet.created_at")
        logger.warning("tweet: %s", tweet)
        # 日付がわからないときは判別不可能なので、何もしない
        return

    if delta.days > 1:
        logger.info("There are no new tweet")
        logger.info("latest: %s", tweet)
        # Tweet 更新なしとする
        return

    try:
        send_message(tweet.text)

        for media in tweet.extended_entities["media"]:
            send_image(media["media_url_https"])
    except Exception as ex:
        logger.error(ex)
        return


if __name__ == "__main__":
    main()
