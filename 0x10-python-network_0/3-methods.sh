#!/bin/bash
#script displays http methods accepted by server 
curl  -X OPTIONS -i "$1"
