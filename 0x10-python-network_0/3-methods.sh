#!/bin/bash
# script displays http methods accepted by server 
curl -sI "$1" | grep "Allow" | cut -d " " -f 2
