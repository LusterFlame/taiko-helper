import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message, send_image_message
from trans import transList, stateList

###################################################################################

load_dotenv()

###################################################################################

machine = TocMachine(
    states=stateList,
    transitions=transList,
    initial="entry",
    auto_transitions=False,
    show_conditions=True,
)

###################################################################################

app = Flask(__name__, static_url_path="")

###################################################################################

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

###################################################################################

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"

###################################################################################

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        #print(f"REQUEST BODY: \n{body}")

        ## Get transcition via input message
        if machine.reset(event) == True:            ## Can reset anytime
            return "OK"

        if machine.state == "entry":                ## In [entry]
            if machine.advance(event) == True:  
                return "OK"
        elif machine.state == "rand_diff":          ## in [rand_diff]
            if machine.toDiff(event) == True:
                return "OK"
        elif machine.state == "rand_diff_easy":     ## in [rand_diff_easy]
            if machine.rand_easy_advance(event) == True:
                return "OK"
        elif machine.state == "rand_diff_normal":   ## in [rand_diff_normal]
            if machine.rand_normal_advance(event) == True:
                return "OK"
        elif machine.state == "rand_diff_hard":     ## in [srand_diff_hard]
            if machine.rand_hard_advance(event) == True:
                return "OK"
        elif machine.state == "rand_diff_oni":      ## in [rand_diff_oni]
            if machine.rand_oni_advance(event) == True:
                return "OK"
        elif machine.state == "rand_oniA":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_oni_advance(event) == True:
                return "OK"
        elif machine.state == "rand_oniB":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_oni_advance(event) == True:
                return "OK"
        elif machine.state == "rand_oniC":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_oni_advance(event) == True:
                return "OK"
        elif machine.state == "rand_oniD":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_oni_advance(event) == True:
                return "OK"
        elif machine.state == "rand_hardA":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_hard_advance(event) == True:
                return "OK"
        elif machine.state == "rand_hardB":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_hard_advance(event) == True:
                return "OK"
        elif machine.state == "rand_hardC":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_hard_advance(event) == True:
                return "OK"
        elif machine.state == "rand_hardD":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_hard_advance(event) == True:
                return "OK"
        elif machine.state == "rand_normalA":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_normal_advance(event) == True:
                return "OK"
        elif machine.state == "rand_normalB":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_normal_advance(event) == True:
                return "OK"
        elif machine.state == "rand_normalC":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_normal_advance(event) == True:
                return "OK"
        elif machine.state == "rand_easyA":
            if machine.sheet(event) == True:
                return "OK"
            elif machine.rand_easy_advance(event) == True:
                return "OK"
        ## Cannot enter any possible transicition
        send_text_message(event.reply_token, text="Not Entering any State")
    return "NO"

###################################################################################

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

###################################################################################

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
