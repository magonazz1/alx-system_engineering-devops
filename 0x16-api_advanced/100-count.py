#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after="", word_count=Counter()):
    """
    Recursively query the Reddit API and return sorted count of keywords.
    """
    base_url = "https://www.reddit.com/"
    headers = {'User-agent': 'Mozilla/5.0'}
    full_url = base_url + "r/" + subreddit + "/hot.json?after=" + after
    response = requests.get(full_url, headers=headers)

    if response.status_code != 200:
        return

    data = response.json()
    titles = [post_data['data']['title'] for post_data in data['data'][
        'children'
        ]]
    for title in titles:
        words = title.lower().split(' ')
        for word in words:
            if word in word_list:
                word_count[word] += 1

    after = data['data'][
            'after'
            ]
    if after is None:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[
            0
            ]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, after, word_count)
