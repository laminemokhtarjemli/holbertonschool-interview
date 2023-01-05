import requests

def count_words(subreddit, word_list, after=None):
  # Set the base URL and headers for the request
  url = f'https://www.reddit.com/r/{subreddit}/hot.json'
  headers = {'User-Agent': 'MyBot/1.0'}

  # Set the parameters for the request
  params = {'limit': 100}
  if after:
    params['after'] = after

  # Make the request and get the response
  response = requests.get(url, headers=headers, params=params)

  # If the response is not successful, return
  if response.status_code != 200:
    return

  # Get the data from the response
  data = response.json()

  # Get the list of hot articles
  hot_articles = data['data']['children']

  # Initialize a dictionary to store the word counts
  word_counts = {}

  # Iterate through the hot articles and count the words
  for article in hot_articles:
    title = article['data']['title']
    for word in word_list:
      if word.lower() in title.lower():
        if word.lower() in word_counts:
          word_counts[word.lower()] += 1
        else:
          word_counts[word.lower()] = 1

  # Get the name of the next page
  after = data['data']['after']

  # If there is a next page, make a recursive call to count_words
  if after:
    count_words(subreddit, word_list, after)

  # Sort the word counts in descending order by count, then alphabetically
  sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

  # Print the sorted word counts
  for word, count in sorted_word_counts:
    print(f'{word}: {count}')
