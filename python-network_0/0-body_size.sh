#!/bin/bash
# sends a request to $1 and displays the response body size in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
