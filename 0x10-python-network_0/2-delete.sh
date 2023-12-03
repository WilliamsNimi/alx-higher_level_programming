#!/bin/bash
#Using curl to send a Delete Request
res=$(curl -X DELETE -s $1)
echo res
