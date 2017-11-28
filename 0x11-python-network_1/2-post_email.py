#!/usr/bin/python3
"""
Takes in url & email address
parses it `,`-> &  ` `-> +
encode into bytes
sends the request then decode the response back to utf-8
"""

if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from urllib.error import URLError

    data = urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = Request(argv[1], data)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print(e)
