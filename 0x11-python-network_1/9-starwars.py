#!/usr/bin/python3
"""
Takes string
Makes a GET request to STAR WARS People API
convert JSON -> dict
print count then iter through list of dicts of results
print name
https://swapi.co/api/people/?search=r2
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.get('https://swapi.co/api/people/',
                       params={'search': argv[1]})
    rjson = res.json()
    print("Number of results:", rjson.get('count'))
    for character in rjson.get('results'):
        print(character.get('name'))
