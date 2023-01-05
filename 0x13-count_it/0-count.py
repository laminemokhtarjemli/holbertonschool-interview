import requests
import re
import sys

def count_words(subreddit, word_list, after=None, count={}):
    # Make the request to the Reddit API
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get('https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params=params)

    # Check if the subreddit is valid
    if response.status_code == 404:
        return

    # Parse the titles of the hot articles
    data = response.json()
    titles = [article['data']['title'] for article in data['data']['children']]
    
    # Count the occurrences of the words in the word list in the titles
    for title in titles:
        for word in word_list:
            word_lower = word.lower()
            count[word_lower] = count.get(word_lower, 0) + len(re.findall(r'\b' + word_lower + r'\b', title.lower()))
    
    # Recursively call the function with the next page of articles
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, count)
    else:
        # Print the results in the required format
        for word, cnt in sorted(count.items(), key=lambda x: (-x[1], x[0])):
            print(f'{word}: {cnt}')
