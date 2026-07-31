#!/bin/bash
# displays all HTTP methods the server accepts for the URL passed as $1
curl -s -X OPTIONS -D - -o /dev/null "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
