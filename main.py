import json
import requests
import sys
import colorama
from colorama import Fore, Back, Style
import os


def introduction():
  print(Fore.MAGENTA + """
 ███▄    █▓██   ██▓ ▄▄▄          ▄████▄   ██▀███   ▄▄▄        █████▒▄▄▄█████▓
 ██ ▀█   █ ▒██  ██▒▒████▄       ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██   ▒ ▓  ██▒ ▓▒
▓██  ▀█ ██▒ ▒██ ██░▒██  ▀█▄     ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒████ ░ ▒ ▓██░ ▒░
▓██▒  ▐▌██▒ ░ ▐██▓░░██▄▄▄▄██    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▒  ░ ░ ▓██▓ ░ 
▒██░   ▓██░ ░ ██▒▓░ ▓█   ▓██▒   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░▒█░      ▒██▒ ░ 
░ ▒░   ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░      ▒ ░░   
░ ░░   ░ ▒░▓██ ░▒░   ▒   ▒▒ ░     ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░ ░          ░    
   ░   ░ ░ ▒ ▒ ░░    ░   ▒      ░          ░░   ░   ░   ▒    ░ ░      ░      
         ░ ░ ░           ░  ░   ░ ░         ░           ░  ░                 
           ░ ░                  ░                                            """)
  print(Style.RESET_ALL)

introduction()

print(
  Fore.CYAN + "[ ! ] Hello, This tool lets you check if your Minecraft account is valid or invalid. ( Personal Use Only )")
print(Style.RESET_ALL)

print(Fore.LIGHTYELLOW_EX + "Please enter your Email: ")
username_input = input("[ > ] ")

print(Fore.LIGHTYELLOW_EX + "Please enter your Password: ")
password_input = input("[ > ] ")

def logic(username, password):
  payload = json.dumps({
    'agent': {
      'name': 'Minecraft',
      'version': 1
    },
    "username": username,
    "password": password,
    "requestUser": "true"
  })
  header = {
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Accept": "*/*",
    "Content-type": "application/json"
  }
  r = requests.post("https://authserver.mojang.com/authenticate", data=payload, headers=header)
  response_code = r.status_code
  if response_code == 200:
    print(Fore.LIGHTGREEN_EX + "This is a valid account!")
    input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
    print(Style.RESET_ALL)
    sys.exit(0)

  elif response_code == 403:
    print(Fore.LIGHTRED_EX + "This account is invalid")
    input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
    print(Style.RESET_ALL)
    sys.exit(0)

  else:
    print("")
    print(Fore.LIGHTRED_EX + "Something went wrong, perhaps your username is invalid or something regarding your network.")
    input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
    print(Style.RESET_ALL)
    sys.exit(0)

logic(username_input, password_input)
