#!/bin/bash
#script send POST REQUEST with the contents of file passed to it
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
