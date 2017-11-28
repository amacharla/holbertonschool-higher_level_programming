#!/usr/bin/python3
"""
Takes in url & letter
Makes a POST request
prints in resonse JSON format
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    letter = argv[1][0] if len(argv) > 1 else ""

    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        rjson = res.json()
        json = "[{}] {}".format(rjson.get('id'), rjson.get('name'))
        print(json if rjson else "No Result")
    except ValueError as e:
        print("Not a valid JSON")
