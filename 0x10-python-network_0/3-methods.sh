#!/bin/bash
# send a OPTIONS request with Awk with Felishas help for awk
curl -IsX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'
