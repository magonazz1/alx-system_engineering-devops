#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API,
and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function to query the Reddit API and return the number of subscribers.
    """
    base_url = "https://www.reddit.com/"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(base_url + "r/" + subreddit + "/about.json",
                            headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data['data']['subscribers']
