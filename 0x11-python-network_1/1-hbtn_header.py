#!/usr/bin/python3
"""
Takes URL
sends request
displays response header for 'X-Request-Id'
"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import URLError

    try:
        with urlopen(argv[1]) as response:
            print(response.info().get('X-Request-Id'))
    except URLError as e:
        print(e)
