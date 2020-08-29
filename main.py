from controllers.scraper import Scrape
from controllers.sms_sender import SMSSender
import argparse


def run():
    parser = argparse.ArgumentParser(description="Telegram Scraper")

    parser.add_argument("--send-sms", help="Send SMS")
    parser.add_argument("--scrape-contact", help="Send SMS")
    parser.add_argument('--file-name', help="File that save contact or read the contact for send message")
    args = parser.parse_args()


    if args.send_sms is not None:
        if args.file_name is not None:
            scraper = Scrape()
            scraper.run()
            print("send sms")
        else:
            print("please add file for read contacts")

    elif args.scrape_contact is not None:
        if args.file_name is not None:
            sms_sender = SMSSender()
            sms_sender.send_smss(args.file_name)
            print("scrape contact")
        else:
            print("please add file that you want to save the contacts")

    else:
        print("error use main.py --help for usage")


if __name__ == '__main__':
    run()
