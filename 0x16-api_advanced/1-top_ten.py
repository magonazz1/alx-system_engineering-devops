#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API,
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    query the Reddit API and print the titles of the first 10 hot posts.
    """
    base_url = "https://www.reddit.com/"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(
            base_url + "r/" + subreddit + "/hot.json?limit=10",
            headers=headers, allow_redirects=False
            )

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    titles = [post_data['data']['title'] for post_data in data['data'][
        'children'
        ]]
    for title in titles:
        print(title)
