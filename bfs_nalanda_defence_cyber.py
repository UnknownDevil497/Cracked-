#!/usr/bin/env python3
# ==========================================
# BFS NALANDA DEFENCE CYBER
# Secure Lookup Tool (Dummy API Demo)
# ==========================================

import requests
import json
import time
import sys
import getpass

PHONE_API = {
    "url": "https://zephrex-num.gauravyt566.workers.dev/",
    "key": "ZEPH-L4L2M",
    "type": "PHONE"
}

AADHAAR_API = {
    "url": "https://zephrex-num.gauravyt566.workers.dev/",
    "key": "ZEPH-MU09X",
    "type": "AADHAAR"
} 

# -══
        ⚔️  UNKNOWN DEVIL FREE CRACKED ⚔️
        ☠️  FREE USE  ☠️

def show_commands()
    print(RED + BOLD + """
AVAILABLE COMMANDS
------------------
1️⃣  Aadhaar Details
2️⃣  Phone Number Details
0️⃣  Exit
""" + RESET)

# ---------- API ----------
def call_api(api_conf, user_value):
    params = {
        "key": api_conf["key"],
        "type": api_conf["type"],
        "term": user_value
    }
    r = requests.get(api_conf["url"], params=params, timeout=20)
    return r.json()

# ---------- CLEAN OUTPUT ----------
def clean_response(data):
    if isinstance(data, dict):
        # dono possible keys hatao
        data.pop("SUPPORT", None)
        data.pop("BUY_API", None)
        data.pop("BUY API", None)
    return data

def print_footer():
    print("\n" + "="*45)
    print(" FREE")
    print(" OWNER- UNKNOWN DEVIL")
    print("="*45 + "\n")

# ---------- MAIN ----------
def main():
    password_check()
    banner()
    skull_loading()

    while True:
        show_commands()
        choice = input("Select Command: ").strip()

        if choice == "1":
            aadhaar = input("Enter Aadhaar Number: ").strip()
            result = call_api(AADHAAR_API, aadhaar)
            cleaned = clean_response(result)
            print(json.dumps(cleaned, indent=4))
            print_footer()

        elif choice == "2":
            number = input("Enter Phone Number: ").strip()
            result = call_api(PHONE_API, number)
            cleaned = clean_response(result)
            print(json.dumps(cleaned, indent=4))
            print_footer()

        elif choice == "0":
            print("Exiting... ☠️")
            sys.exit(0)

        else:
            print("❌ Invalid Command\n")

if __name__ == "__main__":
    main()
