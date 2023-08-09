#!/usr/bin/python3
"""scrip for gather data from an api"""

import requests


def top_ten(subreddit):
    """ret num of sub to given reddit"""
    userAgent = """Mozilla/5.0 (X11; Linux x86_64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"""
    url = 'https://www.reddit.com/r/{}/top.json'
    r = requests.get(url.format(subreddit), headers={'user-agent': userAgent})
    try:
        children = r.json()['data']['children']
        for i in range(10):
            print(children[i]['data']['title'])
    except KeyError:
        print(None)
