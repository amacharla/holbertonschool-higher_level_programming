#!/usr/bin/python3
"""
Takes string
Makes a GET request to GIT API
convert JSON -> dict
print id
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    rjson = res.json()
    print(rjson.get('id'))
