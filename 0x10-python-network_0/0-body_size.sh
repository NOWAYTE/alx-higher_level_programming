#!/bin/bash
# A bash script that takes URL, and sends a request to that URL

curl -s -w "$1" | wc -c
