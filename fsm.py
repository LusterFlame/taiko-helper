from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message
from linebot.models import TemplateSendMessage as TMsg
from linebot.models import MessageAction as MsgAction
from linebot.models import ButtonsTemplate

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_rand_diff(self, event):
        text = event.message.text
        return text.lower() == "random"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def return_to_entry(self, event):
        text = event.message.text
        return text.lower() == "reset"

    def choose_easy(self, event):
        text = event.message.text
        return text.lower() == "easy"

    def choose_normal(self, event):
        text = event.message.text
        return text.lower() == "normal"

    def choose_hard(self, event):
        text = event.message.text
        return text.lower() == "hard"

    def choose_oni(self, event):
        text = event.message.text
        return text.lower() == "oni"

##########################################################

    def on_enter_rand_diff(self, event):
        print("I'm entering rand_diff")
        reply_token = event.reply_token
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = "難しさを選べるドン！♪",
                text = "Please Select Difficuility.",
                actions = [
                    MsgAction(
                        label = "かんたん",
                        text = "easy"
                    ),
                    MsgAction(
                        label = "ふつう",
                        text = "normal"
                    ),
                    MsgAction(
                        label = "むずかしい",
                        text = "hard"
                    ),
                    MsgAction(
                        label = "おに",
                        text = "oni"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_diff(self, event):
        print("Leaving rand_diff")

##########################################################

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")

    def on_exit_state2(self, event):
        print("Leaving state2")

##########################################################

    def on_enter_entry(self, event):
        print("Entering entry")
        reply_token = event.reply_token
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = "何する？",
                text = "What do you want?",
                actions = [
                    MsgAction(
                        label = "ランダムで曲を選ぶ",
                        text = "random"
                    ),
                    MsgAction(
                        label = "譜面を調べる",
                        text = "sheet"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_entry(self, event):
        print("Exiting entry")

##########################################################

    def on_enter_rand_diff_easy(self, event):
        print("Entering ez")
        reply_token = event.reply_token
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = "★数を選べるドン！♪",
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "★1~5",
                        text = "s15"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_diff_easy(self, event):
        pass

##########################################################

    def on_enter_rand_diff_normal(self, event):
        print("Entering n")
        reply_token = event.reply_token
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = "★数を選べるドン！♪",
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "★7",
                        text = "s7"
                    ),
                    MsgAction(
                        label = "★5~7",
                        text = "s57"
                    ),
                    MsgAction(
                        label = "★1~5",
                        text = "s15"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_diff_normal(self, event):
        pass

##########################################################

    def on_enter_rand_diff_hard(self, event):
        print("Entering h")
        reply_token = event.reply_token
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = "★数を選べるドン！♪",
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "★8",
                        text = "s8"
                    ),
                    MsgAction(
                        label = "★7~8",
                        text = "s78"
                    ),
                    MsgAction(
                        label = "★5~7",
                        text = "s57"
                    ),
                    MsgAction(
                        label = "★1~5",
                        text = "s15"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_diff_hard(self, event):
        pass

##########################################################

    def on_enter_rand_diff_oni(self, event):
        print("I'm entering oni")
        reply_token = event.reply_token
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = "★数を選べるドン！♪",
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "★10",
                        text = "s10"
                    ),
                    MsgAction(
                        label = "★8~9",
                        text = "s89"
                    ),
                    MsgAction(
                        label = "★6~8",
                        text = "s68"
                    ),
                    MsgAction(
                        label = "★1~6",
                        text = "s1~6"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_diff_oni(self, event):
        pass

##########################################################