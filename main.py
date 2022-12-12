import logging

import functions_framework

from src.config import TWITTER_USER_ID
from src.get_tweet import get_tweets_of_the_day
from src.send_message import send_image, send_message

logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


@functions_framework.cloud_event
def main(cloud_event):
    """
    Get latest tweet and notify it by line bot
    """
    try:
        tweets = get_tweets_of_the_day(TWITTER_USER_ID)
    except Exception as ex:
        logger.error(ex)
        return

    try:
        for tweet in tweets:
            logger.debug(tweet.text)

            send_message(tweet.text)

            if hasattr(tweet, "extended_entities"):
                for media in tweet.extended_entities["media"]:
                    send_image(media["media_url_https"])

    except Exception as ex:
        logger.error(ex)
        return


if __name__ == "__main__":
    main(None)
