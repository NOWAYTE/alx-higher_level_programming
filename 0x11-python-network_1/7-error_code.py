#!/usr/bin/python3
"""Script sends a request and displays the body of the reposnse"""


import sys
import requests
from requests.exceptions import HTTPError


if __name__ == '__main__':
    try:
        response = requests.get(sys.argv[1])

        if reponse.status_code >= 400:
            print("Error code: {}".format(reponse.status_code))

        else:
            print("{}".format(response.text))
