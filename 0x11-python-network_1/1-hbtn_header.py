#!/usr/bin/python3
"""
Takes URL
sends request
displays response header for 'X-Request-Id'
"""

from sys import argv
from urllib.request import urlopen

with urlopen(argv[1]) as response:
    print(response.info().get('X-Request-Id'))
