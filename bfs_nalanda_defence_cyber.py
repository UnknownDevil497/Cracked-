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

# ---------- COLORS ----------
RED   = "\033[91m"
BOLD  = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

# ---------- PASSWORD ----------
TOOL_PASSWORD = "BFSNALANDADEFENCECYBER!@#$%^&*()_+"
MAX_TRIES = 3

# ---------- DUMMY API CONFIG ----------
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

# ---------- SECURITY ----------
def password_check():
    print("\n🔐 SECURITY CHECK REQUIRED\n")
    for _ in range(MAX_TRIES):
        pwd = input("Enter Tool Password (paste allowed): ")
        if pwd == TOOL_PASSWORD:
            print("\n✅ ACCESS GRANTED\n")
            return
        else:
            print("❌ WRONG PASSWORD\n")
    print("☠️ ACCESS DENIED | TOOL LOCKED ☠️")
    sys.exit(1)

# ---------- VISUALS ----------
def banner():
    print(CLEAR)
    print(RED + BOLD + r"""
██████╗ ███████╗███████╗    ███╗   ██╗ █████╗ ██╗      █████╗ ███╗   ██╗██████╗
██╔══██╗██╔════╝██╔════╝    ████╗  ██║██╔══██╗██║     ██╔══██╗████╗  ██║██╔══██╗
██████╔╝█████╗  ███████╗    ██╔██╗ ██║███████║██║     ███████║██╔██╗ ██║██║  ██║
██╔══██╗██╔══╝  ╚════██║    ██║╚██╗██║██╔══██║██║     ██╔══██║██║╚██╗██║██║  ██║
██████╔╝██╗      ██████║    ██║ ╚████║██║  ██║███████╗██║  ██║██║ ╚████║██████╔╝
╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝

        ⚔️  BFS NALANDA DEFENCE CYBER  ⚔️
        ☠️  AUTHORIZED ACCESS ONLY  ☠️
""" + RESET)

def skull_loading():
    print(RED + BOLD + """
          ☠️ ☠️ ☠️ ☠️ ☠️
      ☠️  SYSTEM INITIALIZING  ☠️
          ☠️ ☠️ ☠️ ☠️ ☠️
""" + RESET)
    for _ in range(2):
        for d in ["", ".", "..", "..."]:
            sys.stdout.write(RED + BLINK + BOLD + f"\rLOADING CYBER MODULES{d}" + RESET)
            sys.stdout.flush()
            time.sleep(0.4)
    print("\n")

def show_commands():
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
    print(" THANK FOR PURCHASING")
    print(" OWNER- BFS NALANDA DEFENCE CYBER FORCE")
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
