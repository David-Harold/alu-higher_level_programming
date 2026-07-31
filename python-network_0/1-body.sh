#!/bin/bash
# displays the body of a GET response to $1 (following redirects) only if the final status code is 200
curl -s -L -o /tmp/body_$$ -w "%{http_code}" "$1" | grep -q 200 && cat /tmp/body_$$
