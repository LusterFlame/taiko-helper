import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message

###################################################################################

load_dotenv()

###################################################################################

machine = TocMachine(
    states=["entry", "rand_diff", "state2", 
            "rand_diff_easy", "rand_diff_normal", "rand_diff_hard", "rand_diff_oni"],
    transitions=[
        {
            "trigger": "advance",
            "source": "entry",
            "dest": "rand_diff",
            "conditions": "is_going_to_rand_diff",
        },
        {
            "trigger": "advance",
            "source": "entry",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {
            "trigger": "reset",
            "source": ["entry", "rand_diff", "state2", "rand_diff_easy", "rand_diff_normal", "rand_diff_hard", "rand_diff_oni"],
            "dest": "entry",
            "conditions": "return_to_entry"
        },
        {
            "trigger": "toDiff",
            "source": "rand_diff",
            "dest": "rand_diff_easy",
            "conditions": "choose_easy"
        },
        {
            "trigger": "toDiff",
            "source": "rand_diff",
            "dest": "rand_diff_normal",
            "conditions": "choose_normal"
        },
        {
            "trigger": "toDiff",
            "source": "rand_diff",
            "dest": "rand_diff_hard",
            "conditions": "choose_hard"
        },
        {
            "trigger": "toDiff",
            "source": "rand_diff",
            "dest": "rand_diff_oni",
            "conditions": "choose_oni"
        }
        # {"trigger": "go_back", "source": ["rand_diff", "state2"], "dest": "entry"},
    ],
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
        if machine.state == "entry":                ## In [entry]
            if machine.reset(event) == True:
                return "OK"
            if machine.advance(event) == True:  
                return "OK"
        elif machine.state == "rand_diff":          ## in [rand_diff]
            if machine.reset(event) == True:
                return "OK"
            elif machine.toDiff(event) == True:
                return "OK"
        elif machine.state == "state2":             ## in [state2]
            if machine.reset(event) == True:
                return "OK"
        elif machine.state == "rand_diff_easy":     ## in [rand_diff_easy]
            pass
        elif machine.state == "rand_diff_normal":   ## in [rand_diff_normal]
            pass
        elif machine.state == "rand_diff_hard":     ## in [srand_diff_hard]
            pass
        elif machine.state == "rand_diff_oni":      ## in [rand_diff_oni]
            pass

        ## Cannot enter any possible transicition
        send_text_message(event.reply_token, text = "Not Entering any State")
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
