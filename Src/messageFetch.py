import Lib.ItChat.itchat as itchat
import time
from pprint import pprint
import json
from threading import Thread, Event
from Timer import MyThread

def saveLoginInfo():
    itchat.dump_login_status("Result/login")
itchat.login(loginCallback=saveLoginInfo)


def fetchmessage():
    itchat.load_login_status("Result/login", loginCallback=None, exitCallback=None)

stopFlag = Event()
thread = MyThread(stopFlag, payloadFunc=fetchmessage, interval=10)
thread.start()
# this will stop the timer
# stopFlag.set()