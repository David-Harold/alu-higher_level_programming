#!/bin/bash
# sends a GET request to $1 with header X-HolbertonSchool-User-Id: 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
