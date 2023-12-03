#!/bin/bash
#Checking allowable methods
res=$(curl -X OPTIONS -s "$1")
allowable=$(echo "res" | grep -Po 'Allow:\s*\K.*')
methods=$(echo "$allowable" | tr ',' ' ')
for method in $methods; do
    echo "$method"
done
