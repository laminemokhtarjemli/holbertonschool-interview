import requests

USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko)\
                 Chrome/87.0.4280.88 Safari/537.36'}

def fetch_subreddit_stories(subreddit, after='null'):
    """Retrieve a list of the top stories on a subreddit.
    
    subreddit: string, name of the subreddit to fetch stories from
    after: string, used to paginate through the stories
    """
    url = f"https://www.reddit.com/r/{subreddit}.json?sort=hot&after={after}&limit=100"
    response = requests.get(url, headers=USER_AGENT, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        stories = data['children']
        next_page = data.get('after')
        return stories, next_page
    return [], None

def count_words_in_stories(subreddit, words_to_count):
    """Count the occurrences of each word in the top stories of a subreddit.
    
    subreddit: string, name of the subreddit to fetch stories from
    words_to_count: list of strings, words to count in the stories
    """
    word_counts = {word: 0 for word in words_to_count}
    stories, next_page = fetch_subreddit_stories(subreddit)
    while stories:
        for story in stories:
            title = story['data']['title'].lower()
            for word in word_counts:
                word_counts[word] += title.split().count(word.lower())
        stories, next_page = fetch_subreddit_stories(subreddit, after=next_page)
    
    sorted_counts = sorted(word_counts.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
