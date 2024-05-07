#!/usr/bin/python3
"""
Recursive function to query Reddit API and return a list of hot article titles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries
    the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')

    for child in children:
        hot_list.append(child['data']['title'])

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
