#!/usr/bin/python3
"""A script that fetches https:alx-intranet.hbtn.io/status"""

import sys
import requests

if __name__ == "__main__":
    request = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body Response:")
    print("\t -type: {}".format(type(request.text)))
    print("\t -contennt {}".format(request.text))
