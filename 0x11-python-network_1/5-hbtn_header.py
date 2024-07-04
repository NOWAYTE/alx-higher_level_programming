#!/usr/bin/python3
"""
Sends a request and displays the value of the variable
X-Request-Id

"""
import sys
import requests

if __name__ == "__main__":
    if (sys.argv[1]):
        request = requests.get(sys.argv[1])

        print(dict(request.headers).get("X-Request-Id"))
