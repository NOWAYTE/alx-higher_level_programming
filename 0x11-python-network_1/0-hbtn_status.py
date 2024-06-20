#!/usr/bin/python3
"""fetches from URL"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        read = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(read)))
        print("\t- content: {}".format(read))
        print("\t- utf8 content: {}".format(read.decode(encoding='utf-8')))
