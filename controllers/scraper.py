
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import csv
import time
from services import auth_service


class Scrape:

    def __init__(self):
        print()


    def run(self):
        try:
            auth_srv = auth_service.AuthService()
            self.client = auth_srv.auth()
        except KeyError:
            os.system('clear')
            print("[!] run python setup.py first !!\n")
            sys.exit(1)

        chats = []
        last_date = None
        chunk_size = 200
        groups = []

        result = self.client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print('[+] Choose a group to scrape members :' )
        i = 0
        for g in groups:
            print('[' + str(i) + ']' + ' - ' + g.title)
            i += 1

        print('')
        g_index = input("[+] Enter a Number : ")
        target_group = groups[int(g_index)]

        print('[+] Fetching Members...')
        time.sleep(1)
        all_participants = []
        all_participants = self.client.get_participants(target_group, aggressive=True)

        print('[+] Saving In file...')
        time.sleep(1)
        with open("members.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
        print('[+] Members scraped successfully.')

