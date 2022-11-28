#!/usr/bin/env python3
import requests
import socket
import re
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    
    if localhost == '127.0.0.1':
        print(True)
    else:
        print(False)


check_localhost()


def check_connectivity():
    numRegex = re.compile(r'[0-9]+')
    # testing connection to http:*
    request = requests.get("http://www.google.com")
    # transforms que resquest variable to a string so the 'import re' can read it:
    mo2 = numRegex.search(str(request))
    result = mo2.group()
 
    if result == '200':
        print(True)
    else:
        print(False)

check_connectivity()

