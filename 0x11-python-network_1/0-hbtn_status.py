#!/usr/bin/python3
""" Display the attributes of response object """

from urllib.request import urlopen

with urlopen('https://intranet.hbtn.io/status') as response:
    page = response.read()

print("Body response:"
      "\n\t- type: ", type(page),
      "\n\t- content: ", page,
      "\n\t- utf8 content: ", page.decode("utf-8"),
      "\n", sep="", end="")
