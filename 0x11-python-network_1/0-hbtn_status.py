#!/usr/bin/python3
"""
A python script that fetches from a URL
"""


from urllib import request

if __name__ == "__main__":

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        read = response.read()
        print("Body response: ")
        print("\t-  type: {}".format(type(read)))
        print("\t-  content: {}".format(read))
        print("\t-  utf8 content: {}".format(read.decode(encoding='utf-8')))
