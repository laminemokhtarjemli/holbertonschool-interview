#!/usr/bin/python3
""" count words
"""
from requests import get


def count_words(subreddit, word_list=[], after=''):
	headers = {''}

	hot = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
	reqhot = get(hot, headers=headers)
	stuff = reqhot.json()
	if stuff.get("data") and stuff['data'].get('children'):
		children = stuff.get("data").get("children")
		for child in children:
			word_list.append(child.get("data").get("title"))

		page = stuff.get("data").get("after")
		if page:
			return count_words(subreddit, word_list, page)

	if word_list == []:
		return None
	return word_list