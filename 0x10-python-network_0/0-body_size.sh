#!/bin/bash
#using curl to get the size of the body of a response
curl -sI "$1" | awk '/Content-Length/ {print $2}'
