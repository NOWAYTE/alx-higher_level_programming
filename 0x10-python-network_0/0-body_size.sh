#!/bin/bash
# A bash script that takes URL, and sends a request to that URL

url = $1

response=$(curl -s -w "$url" | wc -c)

echo "$response"
