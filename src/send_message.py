from linebot import LineBotApi
from linebot.models import ImageSendMessage, TextSendMessage

from config import LINE_BOT_ACCESS_TOKEN


line = LineBotApi(LINE_BOT_ACCESS_TOKEN)


def send_message(message: str):
    line.broadcast(TextSendMessage(text=message))


def send_image(url: str):
    line.broadcast(
        ImageSendMessage(
            original_content_url=url,
            preview_image_url=url,
        )
    )
