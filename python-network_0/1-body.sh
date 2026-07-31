#!/bin/bash
# sends a GET request to the URL passed as $1 and displays the body
# of the response, only if the status code is 200
response=$(curl -s -w "\n%{http_code}" "$1")
status_code=$(echo "$response" | tail -n 1)
body=$(echo "$response" | sed '$d')

if [ "$status_code" -eq 200 ]; then
    echo -n "$body"
fi
