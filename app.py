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

line_bot_api = LineBotApi('6evuybkJ37vShtrQVFtUDVAMd1je7My9BV8weVGEqmIOI2VMFPETk30lHKtqRknDTmvQM7OXFyrGeuU4GqNLrN5zVFBBss6APttCCpfVG+2LglNEk5obE7Mub4YxD2mcdDlC9qfkMI6Pd04vq/g+dAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('41241480adf84d6c7a9db0536df01baa')


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
    msg = event.message.text
    bot_mes = '抱歉，我不太了解你的意思。'

    if msg in ['你是誰', '妳是誰', '是隨', '4隨']:
        bot_mes = '{Nickname}，您好(smile)！\n', 
        '我叫{AccountName}，隸屬艾殷柯吉諾，目前是雨軍團祭司長。\n',
        '這是我的名片：https://www.plurk.com/p/i90nk9\n請多指教！(happy)'
    elif msg in ['吃飯', '吃', '食物']:
        bot_mes = '嗯？\n我吃藥就好了，謝謝你。'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=bot_mes))


if __name__ == "__main__":
    app.run()