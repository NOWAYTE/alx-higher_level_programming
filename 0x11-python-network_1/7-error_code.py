#!/usr/bin/python3
"""Script sends a request and displays the body of the reposnse"""


import sys
import requests
from requests.exceptions import HTTPError


if __name__ == '__main__':
    try:
        response = requests.get(sys.argv[1])

        print("{}".format(response.text))

    except HTTPError as e:
        print("Error code: {}".format(e)
