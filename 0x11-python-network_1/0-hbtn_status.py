#!/usr/bin/python3

from urllib import request

if __name__ == "__main__":
    with request.urlopen('http://alx-intranet.hbtn.io/status') as response:
        response = response.read()
        print(" - type: {}".format(type(response)))
        print(" - content: {}".format(response))
        print(" - utf8 content: {}".format(response.decode(encoding='utf-8')))
