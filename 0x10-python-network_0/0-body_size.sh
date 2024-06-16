#!/usr/bin/env bash
#script that takes in an URL and displys the size of the body

if [ $# -eq 0 ]; then
        echo "Usage: $0 URL"
        exit
fi

curl -sI $1 | grep -i content-length | awk '{print $2}'

exit 0
