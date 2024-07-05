#!/usr/bin/python3
"""Sends a post request to http://0.0.0.0:5000/search_user"""
import sys
import requests


if __name__ == '__main__':

    if (len(sys.argv) == 1):
        letter = ""
    else:
        letter = sys.argv[1]

    value = {"q": letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=value)

    try:
        json = response.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    except ValueError:
        print("Not a valid JSON")
