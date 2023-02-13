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
    if not keywords:
        return None
    
    keywords = [word.lower() for word in keywords]
  
    if not start:
        api_url = 'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        api_url = 'https://www.reddit.com/r/{subreddit}/hot.json?after={start}'

    api_response = requests.get(
        api_url,
        headers={'user-agent': 'user'},
        allow_redirects=False
    )
    try:
        data = api_response.json()['data']
    except BaseException:
        return

    for keyword in keywords:
        if keyword not in keyword_count:
            keyword_count[keyword] = 0

    articles = data['children']
    for article in articles:
        title = article['data']['title'].lower().split(' ')
        for keyword in keywords:
            keyword_count[keyword] += title.count(keyword)

    next_start = data.get('after')
    if next_start:
        return count_words(subreddit, keywords, next_start, keyword_count)
    else:
        sorted_keywords = sorted(keyword_count.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_keywords:
            if count != 0:
                print(f'{keyword}: {count}')
