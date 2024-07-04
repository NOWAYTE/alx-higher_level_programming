#!/usr/bin/python3
"""Send a request and dislays the body response"""
import sys
import urllib
from urllib import request, error

if __name__ == "__main__":
    if (sys.argv[1]):
        request = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(request) as response:
            print("{}".format(response.read().decode("ascii")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
