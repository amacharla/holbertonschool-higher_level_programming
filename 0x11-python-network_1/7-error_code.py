#!/usr/bin/python3
"""
Takes in url
prints the body
or error code for errors greater than 400
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.get(argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError:
        print("Error code:", res.status_code)
