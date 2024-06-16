#!/bin/bash
#displayhs the size of the body response
curl -sI "$1" | grep -i content-length | awk '{print $2}'
