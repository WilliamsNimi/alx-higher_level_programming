#!/bin/bash
#Using curl to send a GET request and display the body
res=$(curl -s "$1")
if [ $? -eq 0 ]; then
    echo $res
fi
