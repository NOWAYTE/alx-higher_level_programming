#!/usr/bin/python3
"""
A python script that takes in github credentials and
uses the Github API to display your id
"""
import sys
import requests

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = " https://api.github.com/user"

    value = {"user":  user, "passwd": passwd}

    try:
        response = requests.get(url, data=value)

        json = response.json()

        print("{}".format(json.get("id")))
    except ValueError:
        print("Hello")
