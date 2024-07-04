#!/usr/bin/python3
"""Takes URL and email and sends a POST request"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    par = {'email': sys.argv[2]}
    res = requests.post(url,data=par)
    print("{}".format(res.text))
