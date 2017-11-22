#!/bin/bash
# get content size only
curl -Is "$1" | grep -E 'Content-Length: .+' | awk '{ print $2 }'
