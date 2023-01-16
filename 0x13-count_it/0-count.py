#!/usr/bin/python3
import requests
import sys

def count_words(subreddit, word_list):
    """
    Counts the number of occurrences of words in the titles of hot articles
    from the specified subreddit and prints them in a sorted order.
    
    subreddit: the subreddit to search in
    word_list: the list of words to search for
    """
    results = {}
    headers = {'User-agent': 'HolbertonSchool'}
    link = 'https://api.reddit.com/r/subreddit/hot.json'
    word_list = [word.lower() for word in word_list]
    
    while True:
        response = requests.get(link, headers=headers)
        
        if response.status_code != 200:
            return
        
        data = response.json()
        children = data['data']['children']
        
        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                if word in title:
                    if word in results:
                        results[word] += 1
                    else:
                        results[word] = 1
        
        if data['data']['after']:
            link = f'https://api.reddit.com/r/{subreddit}/hot.json?after={data["data"]["after"]}'
        else:
            break

    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    for result in sorted_results:
        print(result[0], result[1])
