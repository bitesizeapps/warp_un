import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
from helpers import getTime,getFutureTime

from vars import Var
SEND_LOG = (Var.SEND_LOG)
BOT_TOKEN = (Var.BOT_TOKEN)
CHANNEL_ID = (Var.CHANNEL_ID)
HIDE_ID = (Var.HIDE_ID)
referrer = (Var.WARP_ID)

os.system("title UnlimitedWrapUsage")
os.system('cls' if os.name == 'nt' else 'clear')
print ("[+] Dr.Caduceus")

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()
		return status_code
	except Exception as error:
		print("")
		print("[×] Error:", error)

g = 0
b = 0
while True:
    result = run()
    if result == 200:
        time.sleep(1)
        g = g+1
        print(f"{g} - {getTime()}")
        time.sleep(20)
    else:
        b = b+1
    if b > 20:
        print(f"going for a nap... - be back at {getFutureTime(10)}")
        time.sleep(600)
        g,b = 0
