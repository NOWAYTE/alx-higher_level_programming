#!/usr/bin/python3
"""Sends a POST request to the passed URL"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        data = urllib.parse.urlencode(sys.argv[2])
        data = data.encode('ascii')
        request = urllib.request.Request(sys.argv[1],  data)

        with urllib.request.urlopen(request) as response:
            print("{}".format(response.read().decode("utf-8")))


