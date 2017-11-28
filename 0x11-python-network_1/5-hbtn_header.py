#!/usr/bin/python3
"""
Takes URL
displays response header for 'X-Request-Id'
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
