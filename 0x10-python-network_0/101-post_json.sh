#!/bin/bash
# POST a JSON file
curl -s -X POST -d @"$2" "$1"
