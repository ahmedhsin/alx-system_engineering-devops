#!/usr/bin/python3
"""scrip for gather data from an api"""

import requests


def number_of_subscribers(subreddit):
    """ret num of sub to given reddit"""
    userAgent = """Mozilla/5.0 (X11; Linux x86_64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"""
    url = 'https://www.reddit.com/r/{}/about.json'
    r = requests.get(url.format(subreddit), headers={'user-agent': userAgent})
    try:
        return (r.json()['data']['subscribers'])
    except KeyError:
        return 0
