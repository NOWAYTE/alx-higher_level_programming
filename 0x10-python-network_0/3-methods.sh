#!/bin/bash
# A script that takes in URL and diplays all HTTP methods the server will accept

curl -sLI "$1" | grep -i allow
