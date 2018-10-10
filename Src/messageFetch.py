import Lib.ItChat.itchat as itchat
import time
from pprint import pprint
import json

itchat.load_login_status("Result/login", loginCallback=None, exitCallback=None)

# uncomment this line to trigger a login request, scan code and it will save the login info in the file. 
# Then comment it such that it will only refresh the message. 
# itchat.login(loginCallback=getMessage) 
