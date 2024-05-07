#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''

from requests import get

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers of a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers (integer)
        or 0 if the subreddit is invalid or an error occurs.
    """


    headers = {'User-Agent': 'my_custom_user_agent'}
    response = get(f"https://www.reddit.com/r/{subreddit}/about.json",
                   headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
