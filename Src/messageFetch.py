import Lib.ItChat.itchat as itchat
import time
from pprint import pprint
import json


def lc(): 
    print("logged in")
    messages = itchat.get_msg()

    with open("Result/messages.json", "w") as messageFile:
        json.dump(messages, messageFile, sort_keys=True, indent=4, separators=(',', ': '))
        messageFile.close()

itchat.login(loginCallback=lc)



