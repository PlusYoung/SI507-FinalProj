# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/9 13:37
# @File    : cacheFunction.py

import os
import json


def load_cached_movies(path):
    if os.path.exists(path):
        with open(path, 'r') as infile:
            movie_cache = json.load(infile)
        return movie_cache
    else:
        print("This database dose not exit!")
        return None


def cache_data_to_json(path, movie_data):
    with open(path, 'w') as outfile:
        json.dump(movie_data, outfile)
    print("The relevant data has been automatically fetched and saved to a JSON file.")


# add the 'title' to each json dict module, which will make the json module easily read by movie title
def add_one_layer_to_json(data):
    new_dic = {}
    for i in range(len(data)):
        new_dic[data[i]['title']] = data[i]
    with open('add_layer_data.json', 'w') as outfile:
        json.dump(new_dic, outfile)
    return new_dic


if __name__ == '__main__':
    # Load cached movies from the JSON file
    movie_cache = load_cached_movies('movie_data.json')
    # print(movie_cache)

    # Example: Retrieve cached movies
    if movie_cache:
        # Encoding the string as UTF-8 and decoding it with 'unicode_escape'
        # to replace escape sequences with the actual characters
        print(json.dumps(movie_cache, indent=4))
    else:
        print("No cached movies found.")
