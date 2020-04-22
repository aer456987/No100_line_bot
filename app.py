from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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
    Self_intr = '您好！\n我叫亞伯‧派拉德，住在艾殷柯吉諾,目前隸屬於暴風神殿，是雨軍團的祭司長。\n這是我的名片：https://www.plurk.com/p/i90nk9\n請多指教！'
    # 自我介紹

    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='265',
            sticker_id='4'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return


    if msg in ['你是誰', '妳是誰', '是隨', '你4隨', '尼4隨', 'ni是誰', 'ni4隨', 'NI4隨'] :
        bot_mes = Self_intr
    elif  '你好' in msg:
        bot_mes = Self_intr
    elif '介紹你' in msg:
        bot_mes = Self_intr
    elif '多了解你' in msg:
        bot_mes = Self_intr


    if '食物' in msg:
        bot_mes = '我沒有特別喜歡的食物。'
    elif '吃飯' in msg:
        bot_mes = '嗯？\n不用了，你吃就好，謝謝你。'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=bot_mes))


if __name__ == "__main__":
    app.run()