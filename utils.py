import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text = text))
    return "OK"

def send_button_message(reply_token, ButtonMsg):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ButtonMsg)
    return "OK"

def send_image_message(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    print(img_url)
    line_bot_api.reply_message(reply_token, ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url,
    ))
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
