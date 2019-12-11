from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_image_message
from linebot.models import TemplateSendMessage as TMsg
from linebot.models import MessageAction as MsgAction
from linebot.models import ButtonsTemplate
import random

from wrap import wrapWikiInfo, wrapImage

# Fetch info from taiko-wiki
MListInfo = wrapWikiInfo()

# List for each difficulty level block
os10List = []
os89List = []
os68List = []
os16List = []
hs8List = []
hs78List = []
hs57List = []
hs15List = []
ns7List = []
ns57List = []
ns15List = []
es15List = []

# url for sheet image
sheetURL = ""

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_rand_diff(self, event):
        text = event.message.text
        return text.lower() == "random"

    def return_to_entry(self, event):
        text = event.message.text
        return text.lower() == "reset"

    # For random oni musics
    def choose_oni(self, event):
        text = event.message.text
        return text.lower() == "oni"

    def advance10(self, event):
        text = event.message.text
        return text.lower() == "s10"

    def advance89(self, event):
        text = event.message.text
        return text.lower() == "s89"

    def advance68(self, event):
        text = event.message.text
        return text.lower() == "s68"

    def advance16(self, event):
        text = event.message.text
        return text.lower() == "s16"

    # For random hard musics  
    def choose_hard(self, event):
        text = event.message.text
        return text.lower() == "hard"

    def advance8(self, event):
        text = event.message.text
        return text.lower() == "s8"

    def advance78(self, event):
        text = event.message.text
        return text.lower() == "s78"

    def advance57(self, event):
        text = event.message.text
        return text.lower() == "s57"

    def advance15(self, event):
        text = event.message.text
        return text.lower() == "s15"

    # For random normal musics, s15 and s57 on above 
    def choose_normal(self, event):
        text = event.message.text
        return text.lower() == "normal"

    def advance7(self, event):
        text = event.message.text
        return text.lower() == "s7"

    # For random easy musics, s15 above
    def choose_easy(self, event):
        text = event.message.text
        return text.lower() == "easy"

    def to_seeSheet(self, event):
        text = event.message.text
        return text.lower() == "see_sheet"

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

        # Refetch info from wiki
        MListInfo = wrapWikiInfo()

        # Clear all lists
        os10List.clear()
        os89List.clear()
        os68List.clear()
        os16List.clear()
        hs8List.clear()
        hs78List.clear()
        hs57List.clear()
        hs15List.clear()
        ns7List.clear()
        ns57List.clear()
        ns15List.clear()
        es15List.clear()

        # Send starting msg after fetch
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

        for count, m in enumerate(MListInfo):
            es15List.append([m[0], m[2][0], m[2][1]])

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

        for count, m in enumerate(MListInfo):
            level = m[3][0]
            if level == "7":
                ns7List.append([m[0], m[3][0], m[3][1]])
                ns57List.append([m[0], m[3][0], m[3][1]])
            elif level == "6":
                ns57List.append([m[0], m[3][0], m[3][1]])
            elif level == "5":
                ns57List.append([m[0], m[3][0], m[3][1]])
                ns15List.append([m[0], m[3][0], m[3][1]])
            else:
                ns15List.append([m[0], m[3][0], m[3][1]])

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

        for count, m in enumerate(MListInfo):

            level = m[4][0]
            if level == "8":
                hs8List.append([m[0], m[4][0], m[4][1]])
                hs78List.append([m[0], m[4][0], m[4][1]])
            elif level == "7":
                hs78List.append([m[0], m[4][0], m[4][1]])
                hs57List.append([m[0], m[4][0], m[4][1]])
            elif level == "6":
                hs57List.append([m[0], m[4][0], m[4][1]])
            elif level == "5":
                hs57List.append([m[0], m[4][0], m[4][1]])
            elif level == "6":
                hs57List.append([m[0], m[4][0], m[4][1]])
            elif level == "5":
                hs57List.append([m[0], m[4][0], m[4][1]])
                hs15List.append([m[0], m[4][0], m[4][1]])
            else:
                hs15List.append([m[0], m[4][0], m[4][1]])

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
        print("I'm exiting hard")

##########################################################

    def on_enter_rand_diff_oni(self, event):
        print("I'm entering oni")

        for count, m in enumerate(MListInfo):

            level = m[5][0]
            if level == "10":
                os10List.append([m[0], m[5][0], m[5][1]])
            elif level == "9":
                os89List.append([m[0], m[5][0], m[5][1]])
            elif level == "8":
                os68List.append([m[0], m[5][0], m[5][1]])
                os89List.append([m[0], m[5][0], m[5][1]])
            elif level == "7":
                os68List.append([m[0], m[5][0], m[5][1]])
            elif level == "6":
                os68List.append([m[0], m[5][0], m[5][1]])
                os16List.append([m[0], m[5][0], m[5][1]])
            else:
                os16List.append([m[0], m[5][0], m[5][1]])

            # Possibly some ura sheets
            if m[6] != "no_exist":
                level = m[6][0]
                if level == "10":
                    os10List.append([m[0], m[6][0], m[6][1], "ura"])
                elif level == "9":
                    os89List.append([m[0], m[6][0], m[6][1], "ura"])
                elif level == "8":
                    os68List.append([m[0], m[6][0], m[6][1], "ura"])
                    os89List.append([m[0], m[6][0], m[6][1], "ura"])
                elif level == "7":
                    os68List.append([m[0], m[6][0], m[6][1], "ura"])
                elif level == "6":
                    os68List.append([m[0], m[6][0], m[6][1], "ura"])
                    os16List.append([m[0], m[6][0], m[6][1], "ura"])
                else:
                    os16List.append([m[0], m[6][0], m[6][1], "ura"])

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
                        text = "s16"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_diff_oni(self, event):
        print("I'm exiting oni")

##########################################################

    def on_enter_rand_oniA(self, event):
        print("I'm entering oniA")
        reply_token = event.reply_token
        global sheetURL

        chosenMInfo = random.choice(os10List)
        if len(chosenMInfo) > 3:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0] + "[裏]"
            sheetURL = wrapImage(chosenMInfo[2], True)
        else:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
            sheetURL = wrapImage(chosenMInfo[2], False)

        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s10"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_oniB(self, event):
        print("I'm entering oniB")
        reply_token = event.reply_token
        global sheetURL

        chosenMInfo = random.choice(os89List)
        if len(chosenMInfo) > 3:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0] + "[裏]"
            sheetURL = wrapImage(chosenMInfo[2], True)
        else:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
            sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s89"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_oniC(self, event):
        print("I'm entering oniC")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(os68List)
        if len(chosenMInfo) > 3:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0] + "[裏]"
            sheetURL = wrapImage(chosenMInfo[2], True)
        else:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
            sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s68"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_oniD(self, event):
        print("I'm entering oniD")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(os16List)
        if len(chosenMInfo) > 3:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0] + "[裏]"
            sheetURL = wrapImage(chosenMInfo[2], True)
        else:
            MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
            sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s16"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_oniA(self, event):
        pass

    def on_exit_rand_oniB(self, event):
        pass

    def on_exit_rand_oniC(self, event):
        pass

    def on_exit_rand_oniD(self, event):
        pass

##########################################################

    def on_enter_rand_hardA(self, event):
        print("I'm entering hardA")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(hs8List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)

        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s8"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_hardB(self, event):
        print("I'm entering hardB")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(hs78List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s78"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_hardC(self, event):
        print("I'm entering hardC")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(hs57List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s57"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_hardD(self, event):
        print("I'm entering oniD")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(hs15List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s15"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_hardA(self, event):
        pass

    def on_exit_rand_hardB(self, event):
        pass

    def on_exit_rand_hardC(self, event):
        pass

    def on_exit_rand_hardD(self, event):
        pass

##########################################################

    def on_enter_rand_normalA(self, event):
        print("I'm entering normalA")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(ns7List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s7"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_normalB(self, event):
        print("I'm entering normalA")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(ns57List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s57"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_enter_rand_normalC(self, event):
        print("I'm entering normalA")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(ns15List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s15"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_normalA(self, event):
        pass

    def on_exit_rand_normalB(self, event):
        pass

    def on_exit_rand_normalC(self, event):
        pass

##########################################################

    def on_enter_rand_easyA(self, event):
        print("I'm entering normalA")
        reply_token = event.reply_token
        global sheetURL
        
        chosenMInfo = random.choice(es15List)
        MusicTitle = "★" + chosenMInfo[1] + "  " + chosenMInfo[0]
        sheetURL = wrapImage(chosenMInfo[2], False)
        
        bMsg = TMsg(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = "https://i.imgur.com/vWbUSUf.png",
                title = MusicTitle,
                text = "Please Select level to choose from.",
                actions = [
                    MsgAction(
                        label = "リセット",
                        text = "reset"
                    ),
                    MsgAction(
                        label = "譜面を見るドン！♪",
                        text = "see_sheet"
                    ),
                    MsgAction(
                        label = "同じ難しさで選ぶドン！♪",
                        text = "s15"
                    )
                ]
            )
        )
        send_button_message(reply_token, bMsg)

    def on_exit_rand_easyC(self, event):
        pass

##########################################################

    def on_enter_seeSheet(self, event):
        print("I'm entering seeSheet")
        reply_token = event.reply_token
        send_image_message(reply_token, sheetURL)

    def on_exit_seeSheet(self, event):
        pass
