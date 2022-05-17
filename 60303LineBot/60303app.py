from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('+VSjoYI3DPyyEA+322H8MTuGMqRC/wo5Y7zcSmJ65QVXPdLD8H2WN/WvsCNyPYDKf+yToUQ/vvHWfVcoSTpkEFBscGgmlyiQ2JgVPdx1ll3ohOyijuay7c5PH2cZk1v6i30Wb+QKySWUwBcKZUC4AAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1e3fdec6c0f294a979c815788e1b784a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
