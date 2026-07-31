#!/bin/bash
# sends a DELETE request to the URL passed as $1 and displays the
# body of the response
curl -s -X DELETE "$1"
