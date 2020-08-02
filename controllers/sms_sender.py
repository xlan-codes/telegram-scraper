import csv
import sys
import time
from telethon.errors import PeerFloodError
from telethon.tl.types import InputPeerUser
from services import auth_service
from constants import SLEEP_TIME


class SMSSender:

    def send_smss(self, input_file):
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        print("[1] send sms by user ID\n[2] send sms by username ")
        mode = int(input("Input : "))

        message = input("[+] Enter Your Message : ")
        auth_srv = auth_service.AuthService()
        client = auth_srv.auth()
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'], user['access_hash'])
            else:
                print("[!] Invalid Mode. Exiting.")
                client.disconnect()
                sys.exit()
            try:
                print("[+] Sending Message to:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print("[+] Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print(
                    "[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again "
                    "after some time.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print("[!] Error:", e)
                print("[!] Trying to continue...")
                continue
        client.disconnect()
        print("Done. Message sent to all users.")