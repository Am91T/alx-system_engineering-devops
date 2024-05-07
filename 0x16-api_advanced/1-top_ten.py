#!/usr/bin/python3
"""
Function to query the Reddit API and print
the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    for a given subreddit.
    """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        print(None)
        return

    for child in children:
        print(child['data']['title'])
