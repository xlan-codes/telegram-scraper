#!/bin/env python3
# developed code by : xlan-codes

"""
you can re run setup.py
"""

def config_files_setup():
    import configparser
    cpass = configparser.RawConfigParser()
    cpass.add_section('credential')
    xid = input("\n[+] Enter API ID : " )
    cpass.set('credential', 'ID', xid)
    xhash = input("\n[+] Enter Hash ID : ")
    cpass.set('credential', 'hash', xhash)
    xphone = input("\n[+] Enter Phone Number : ")
    cpass.set('credential', 'phone', xphone)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print("\n[+] setup complete !")



try:
    config_files_setup()
except IndexError:
    print('\n Something goes wrong please try again')