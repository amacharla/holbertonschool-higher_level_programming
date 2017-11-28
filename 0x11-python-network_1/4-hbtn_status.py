#!/usr/bin/python3
""" Display the attributes of response object """

if __name__ == "__main__":
    import requests
    page = requests.get('https://intranet.hbtn.io/status')
    print("Body response:"
          "\n\t- type: ", type(page.text),
          "\n\t- content: ", page.text,
          "\n", sep="", end="")
