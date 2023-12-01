#!/bin/bash
# A bash script that takes in URL and displays all the HTTPS methods the server will accept
curl -sI "$1" | grep  "allow" | cut -d "" -f 2-
