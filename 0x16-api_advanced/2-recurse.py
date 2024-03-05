#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API,
and returns a list containing the titles of all hot articles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function to query the Reddit API and return a list of titles.
    """
    base_url = "https://www.reddit.com/"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(
            base_url + "r/" + subreddit + "/hot.json?after=" + after,
            headers=headers, allow_redirects=False
            )

    if response.status_code != 200:
        return None

    data = response.json()
    hot_list += [post_data['data']['title'] for post_data in data['data'][
        'children'
        ]]
    after = data['data']['after']

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
