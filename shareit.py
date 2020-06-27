#!/bin/python3.6

import os
import hashlib
import urllib.request
import requests
import argparse
import json

parser = argparse.ArgumentParser(description="Create sharable local file.")
parser.add_argument("--port", "-p", default="80", help="custom port of the webserver")
parser.add_argument("-P", action="store_true", help="test if the port is open (may slow down runtime)")
parser.add_argument("file", help="path of the file to be shared")

args = parser.parse_args()

# If file does not exist, exit program
if not os.path.isfile(args.file):
    print("File does not exist")
    exit()

# Creating the symlink to the apache folder
hash_name=hashlib.md5(args.file.encode()).hexdigest()[:10]
share_path="/var/www/html/share/"+hash_name
if not os.path.islink(share_path):
    os.symlink(os.path.abspath(args.file),share_path)
else:
    print("Symlink already exists")


r = requests.get(url="https://ident.me")
ip=r.text

port_api_params={"q":ip}

# Testing if the port is open
if args.P:
    r = requests.get(url="https://api.hackertarget.com/nmap/", params=port_api_params, stream=True)
    if r.ok:
        ports = r.text
        p_open = False
        for line in ports.splitlines()[5:-2]:
            if (line.split()[0].__contains__(args.port)) and (line.split()[0].__contains__(args.port)) and (line.split()[1] == "open"):
                p_open = True
                print("")
        if not p_open == True:
            print("Port is not open")
    else:
        print("Unable to test port access")

if args.port != "80":
    port = args.port
else:
    port = ""

# Writes the url for the file
print("http://"+ip+":"+port+"/share/"+hash_name)
