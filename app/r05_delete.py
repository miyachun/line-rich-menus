from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('XXX')

line_bot_api.delete_rich_menu('richmenu-XXX')