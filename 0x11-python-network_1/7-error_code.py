#!/usr/bin/python3
"""Script sends a request and displays the body of the reposnse"""


import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))

    else:
        print("{}".format(response.text))
