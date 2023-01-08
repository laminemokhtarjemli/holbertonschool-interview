#!/usr/bin/python3

import requests as r


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko)\
                 Chrome/87.0.4280.88 Safari/537.36'}


def recursive_call(reddit, top_list=[], after="null"):
    URL = "https://www.reddit.com/r/{}.json?sort=hot&after={}&limit=100"\
          .format(reddit, after)

    try:
        subscribers = r.get(URL, headers=HEADERS,
                            allow_redirects=False).json()
        data = subscribers.get("data")
        after = subscribers.get("data").get("after")
        top_list += [story.get("data")['title'] for story in data['children']]
        if after:
            recursive_call(reddit, top_list, after)
        return top_list
    except Exception:
        pass


def count_words(reddit, word_list, array=None, dic={}):

    if dic == {}:
        for word in word_list:
            dic.update({word: 0})
    if array is None:
        array = recursive_call(reddit)
    if array and len(array) > 0:
        if word_list != []:
            word_list = list(set(word_list))
            for item in array:
                item = item.lower()
                if word_list[-1].lower() in item.split():
                    if word_list[-1] in dic.keys():
                        dic[word_list[-1]] += 1
            word_list.pop(-1)
            count_words(reddit, word_list, array, dic)
        else:
            for key in sorted(dic.items(), key=lambda kv: (-kv[1], kv[0])):
                if key[1] != 0:
                    print("{}: {}".format(key[0], key[1]))
