#!/usr/bin/python3
"""A script that fetches https:alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body Response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- contennt {}".format(req.text))
