#!/usr/bin/python3
"""
Takes in url
sends the request then decode the response back to utf-8
handles HTTP Error
"""

from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    with urlopen(argv[1]) as response:
        print(response.read().decode('utf-8'))
except HTTPError as e:
    print("Error code:", e.code)
