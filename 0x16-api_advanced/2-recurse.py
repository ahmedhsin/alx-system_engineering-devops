#!/usr/bin/python3
"""scrip for gather data from an api"""

import requests


def recurse(subreddit, hot_list=[], next=''):
    """ret num of sub to given reddit"""
    userAgent = """Mozilla/5.0 (X11; Linux x86_64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"""
    url = 'https://www.reddit.com/r/{}/hot.json?' + next
    r = requests.get(url.format(subreddit), headers={'user-agent': userAgent})
    try:
        children = r.json()['data']['children']
        hot_list = hot_list + children
        after = r.json()['data']['after']
        next = f'after={after}'
        return recurse(subreddit, hot_list, next)
    except KeyError:
        return (None if len(hot_list) == 0 else hot_list)
