#!/usr/bin/python3

from urllib import request

if __name__ == "__main__":
    with request.urlopen('http://alx-intranet.hbtn.io/status') as response:
        response = response.read()
        print("Body response:$")
        print("\t- type: {}$".format(type(response)))
        print("\t- content: {}$".format(response))
        print("\t- utf8 content: {}$".format(response.decode('utf-8')))

