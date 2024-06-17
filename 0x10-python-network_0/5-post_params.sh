#!/bin/bash
#script that send a POST request and displays the body of the response 
curl -s -X POST -d"email=test@gmail.com&subject=I Will always be here for PLD" "$1"
