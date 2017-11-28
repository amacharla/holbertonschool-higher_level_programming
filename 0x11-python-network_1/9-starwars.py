#!/usr/bin/python3
"""
Takes string
Makes a POST request to STAR WARS People API
prints in resonse JSON format
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.post('https://swapi.co/api/people/', data = {'search': argv[1]})
    try:
        rjson = res.json()
        json = "[{}] {}".format(rjson.get('id'), rjson.get('name'))
        print(json if rjson else "No Result")
    except ValueError as e:
        print("Not a valid JSON")
