# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/9 13:26
# @File    : dataTMDb.py
import requests
import constant
from cacheFunction import cache_data_to_json
from checkInput import self_input

API_KEY = 'aa81dde10be1a5e7a104fb616de2beca'


# get information about actors and directors
def fetch_movie_details(movie_id):
    base_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        'api_key': API_KEY,
        'append_to_response': 'credits',
    }
    response = requests.get(base_url, params=params)
    return response.json()


# fetch movie from one year and one genre
def fetch_movies(page=1, year=None, genre_ids=None, sort_by='popularity.desc'):
    base_url = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': API_KEY,
        'page': page,
        'sort_by': sort_by,
    }

    if year:
        params['primary_release_year'] = year

    if genre_ids:
        params['with_genres'] = ','.join(str(id) for id in genre_ids)

    response = requests.get(base_url, params=params)
    movie_results = response.json()['results']
    movie_data = []
    for movie in movie_results:
        details = fetch_movie_details(movie['id'])
        movie['actors'] = [cast['name'] for cast in details['credits']['cast']]
        movie['directors'] = [crew['name'] for crew in details['credits']['crew'] if crew['job'] == 'Director']
        movie['genres'] = [constant.genre_id_to_name[genre_id] for genre_id in movie['genre_ids']]
        # print(movie)
        try:
            movie_info = {
                'id': movie['id'],
                'title': movie['title'],
                'year': year,
                'genres': movie['genres'],
                'actors': movie['actors'][:5],
                'directors': movie['directors'][0],
                'overview': movie['overview'],
                'popularity': movie['popularity'],
                'vote average': movie['vote_average'],
                'vote count': movie['vote_count']
            }
            movie_data.append(movie_info)
            # print(movie_data)
        except:
            pass
    return movie_data


def fetch_movies_more(years, genre_ids=None, flag=1):
    movie_data = []

    if flag == 1:
        for year in years:
            print(f"Fetching movies from {year}...")
            movies = fetch_movies(year=year, genre_ids=genre_ids)
            # try:
            #     movies = fetch_movies(year=year, genre_ids=genre_ids)
            # except:
            #     print('The condition you gave is too strict. Please use less genre and more years to pick movies.')
            #     return None
    if flag == 2:
        for year in years:
            print(f"Fetching movies from {year}...")
            for genre in genre_ids:
                print(f"Fetching movies in {genre}...")
                movies = fetch_movies(year=year, genre_ids=genre_ids)
                # try:
                #     movies = fetch_movies(year=year, genre_ids=genre_ids)
                # except:
                #     print('The condition you gave is too strict. Please use less genre and more years to pick movies.')
                #     return None
    path = self_input(
        "The relevant data will be automatically fetched and saved to a JSON file for further processing. The "
        "default file name is 'movie_data.json'. Do you want to change the file name? If you wish to change it, "
        "please enter the new file name; otherwise, enter 'None': ")
    cache_data_to_json(path, movies)

    return movies, path
