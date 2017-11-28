#!/usr/bin/python3
"""
Takes in url & email address
Makes a POST request
prints the body
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.post(argv[1], data = {'email': argv[2]})
    print(res.text)
