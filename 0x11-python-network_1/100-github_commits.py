#!/usr/bin/python3
"""
make a request to github api
takes two arguments: username and repo
convert JSON -> dict
print recent 10 commits
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = requests.get(url)
    rjson = res.json()
    for commit in rjson[:10]:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
