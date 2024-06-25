#!/usr/bin/python3
"""Send a request to the URL and returns X-Reques-Id"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        request = urllib.request.Request(sys.argv[1])

        with urllib.request.urlopen(request) as response:
            print(dict(response.headers).get("X-Request-Id"))
