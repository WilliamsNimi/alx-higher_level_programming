#!/bin/bash
#Send a GET Request and display header
curl -s "$1" -X GET -H "X-School-User-Id: 98"
