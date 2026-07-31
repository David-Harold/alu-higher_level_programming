#!/bin/bash
# sends a DELETE request to $1 and displays the response body
curl -s -X DELETE "$1"
