
from telethon.sync import TelegramClient
import configparser
import os, sys


class AuthService():

    def __init__(self):
        print();


    def auth(self):

        try: # get credentials
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['credential']['id']
            api_hash = cpass['credential']['hash']
            phone = cpass['credential']['phone']
        except KeyError:
            os.system('clear')
            print("[!] run python3 setup_script.py first !!\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)

        client.connect() # connect to telegram
        if not client.is_user_authorized(): # check if user authenticated
            client.send_code_request(phone)
            os.system('clear')
            client.sign_in(phone, input('[+] Enter the code: '))

        return client

