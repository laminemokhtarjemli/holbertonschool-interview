#!/usr/bin/python3
import requests

def generate_word_count_dicts(words):
    """
    Creates dictionaries to store the word count and the number of duplicates of each word in the list.
    """
    word_count = {word: 0 for word in words}
    duplicate_count = {}
    for word in words:
        if word not in duplicate_count:
            duplicate_count[word] = 0
        duplicate_count[word] += 1
    return word_count, duplicate_count


def count_words(subreddit, words, after="", word_count={}, duplicate_count={}, is_recursive=False):
    """
    Queries the Reddit API to get the word count in a subreddit.
    """
    if not is_recursive:
        word_count, duplicate_count = generate_word_count_dicts(words)

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = requests.get(url, headers=headers).json()

    try:
        data = response.get('data')
        articles = data.get('children')
        new_after = data.get('after')

        for article in articles:
            article_data = article.get('data')['title']
            for word in word_count:
                count = article_data.lower().split(' ').count(word.lower())
                word_count[word] += count

        if new_after:
            count_words(subreddit, words, new_after, word_count, duplicate_count, True)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: x[::-1])
            sorted_desc = sorted(sorted_words, key=lambda x: x[1], reverse=True)

            for word, count in sorted_desc:
                count *= duplicate_count[word]
                if count:
                    print(f'{word.lower()}: {count}')
    except Exception:
        return None
