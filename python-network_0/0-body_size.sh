#!/bin/bash
# sends a request to the URL passed as $1 and displays the size,
# in bytes, of the body of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
