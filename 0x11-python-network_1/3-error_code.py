#!/usr/bin/python3
"""Send a request and dislays the body response"""
import sys
import urllib
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    if (sys.argv[1]):
        request = urllib.request.Request(sys.argv[0])

    try:
        with urllib.request.urlopen(request) as response:
            print("{}".format(reponse.read()))
    except urllib.error.HTTPError as e:
        print("{}".format(e.code))
