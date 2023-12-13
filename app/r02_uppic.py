from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('XXX')

with open("pic.png", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-XXX", "image/png", f)