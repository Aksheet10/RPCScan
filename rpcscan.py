#!/bin/python3
# Author : HACKE-RC commonly known as RC
# Description : RPCSCAN by RC - A python tool to automate all the efforts that you put on finding the xmlrpc.php file on all of your targets subdomains and then finding the vulnerable methods and then finding the reports on hackerone and medium writeups.
# Developer contact: @coder_rc on twitter. You can request new feature by tagging me on any of your tweet.
# Note: If you have some better reports/writeups avaible please tag me on twitter with its link.

import sys
import urllib3
from colorama import Fore
import re
import requests
import os

urllib3.disable_warnings()
http = urllib3.PoolManager(cert_reqs='CERT_NONE')

def help():
    banner = r"""
 ____  ____   ____ ____   ____    _    _   _ 
|  _ \|  _ \ / ___/ ___| / ___|  / \  | \ | |
| |_) | |_) | |   \___ \| |     / _ \ |  \| |
|  _ <|  __/| |___ ___) | |___ / ___ \| |\  |
|_| \_\_|    \____|____/ \____/_/   \_\_| \_|                                            
"""
    print(f"{Fore.RED}" + banner)
    print("\t\t\t\t\tv1.0")
    print(f"{Fore.BLUE}------------ RPCScan by RC ------------")
    print("----- github.com/HACKE-RC/XMLRPC -----")
    print("\33[9mA python tool to automate all the efforts that you put on the xmlrpc.php file.")
    print("Usage:")
    print("\txmlrpc <weblist>")
    sys.exit(1)

def send(url):
    return http.request("GET", url)

def scan(url):
    os.system(f"python3 scanner.py {url}")

if (len(sys.argv)<2):
    help()
if len(sys.argv)>1:
    if sys.argv[1]=="-h" or sys.argv[1]=="--help":
        help()
file = open(sys.argv[1])
def full(url):
    try:
        url = url.replace("\n", "")
        url = url.replace("%0a", "")
        response = http.request("GET", f"{url}/xmlrpc.php")
        Confidence=0
        if response.status==405:
            Confidence+=60
            if re.search("POST requests only", str(response.data)):
                Confidence+=20
                stri=f"\n{Fore.GREEN}[!] Found xmlrpc on {url} [!]\n[!] Status code: {Fore.BLUE}405{Fore.GREEN} [!]\n[!] REGEX Found: {Fore.BLUE}XML-RPC server accepts POST requests only.{Fore.GREEN} [!]\n[!] Confidence : {Fore.BLUE}{Confidence}%{Fore.GREEN} [!]"
                print(stri)
                scan(url)

            else:
                print(f"{Fore.GREEN}[!] Found xmlrpc on {url} [!]\n[!] Confidence : {Confidence}% [!]\n[!] It is not recommended to exploit when the confidence is lower than 80% [!]\n[!] You can manually try to exploit this [!]")
        else:
            print(f"{Fore.RED}[-] No xmlrpc on {url} [-]")
    #except Exception as e:
        #print(e)
    except:
        url = url.replace("\n", "")
        print(f"{Fore.BLUE}[-] No xmlrpc on {url} [-]")



for url in file:
    full(url)
