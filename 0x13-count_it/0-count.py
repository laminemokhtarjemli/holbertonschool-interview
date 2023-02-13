#!/usr/bin/python3
import requests
"""query the Reddit API and perform word counting """

def count_words(subreddit, keywords, start=None, keyword_count={}):
    """
    Recursively queries the Reddit API for a subreddit, 
    parses the titles of articles, and prints a sorted
    count of given words. Javascript should count as 
    javascript, but java should not.

    Parameters:
        subreddit: The subreddit to search.
        keywords: List of keywords to count in the titles.
        start: Indicator for pagination, specifies the starting
            point for the API request.
        word_count: Dictionary to store the count of each keyword.
    """
    if keyword_count == []:
        return None
    else:
        lower_list = (map(lambda word: word.lower(), keywords))
        keywords = list(lower_list)
    if start is None:
        hot = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        hot = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, start)
    hot_request = requests.get(hot,
                               headers={"user-agent": "user"},
                               allow_redirects=False)
    try:
        data = hot_request.json().get("data")
    except BaseException:
        return
    for word in keywords:
        if word not in keyword_count.keys():
            keyword_count[word] = 0
    children = data.get("children")
    for child in children:
        title = (child.get("data").get("title").lower())
        title = title.split(' ')
        for word in keywords:
            keyword_count[word] += title.count(word)
    start = data.get("after")
    if start is not None:
        return count_words(subreddit,keywords, start, keyword_count)
    else:
        sorted_subs = sorted(keyword_count.items(), key=lambda x: (-x[1], x[0]))
        for i in sorted_subs:
            if i[1] != 0:
                print(i[0] + ": " + str(i[1]))
