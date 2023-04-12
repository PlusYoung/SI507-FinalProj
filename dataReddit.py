# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/10 17:51
# @File    : dataReddit.py

import praw

REDDIT_CLIENT_ID = 'OoVKZzqmvk2-dll_XiIjIQ'
REDDIT_SECRET = 'PSRIKy3ciYIv_kC1X5JXboN43nBv1A'
REDDIT_USER_AGENT = 'reddit:MovieRecommender:v1.0 (by /u/dsdjsdoi)'

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT
)


def fetch_movie_reviews(subreddit_name, movie_title, limit=3):
    subreddit = reddit.subreddit(subreddit_name)
    search_query = f'title:{movie_title}'
    submissions = subreddit.search(search_query, limit=limit)

    reviews = []
    for submission in submissions:
        # Fetch all comments, including those hidden behind "load more comments" links
        # submission.comments.replace_more(limit=2)
        comments = submission.comments.list()
        review = {
            'title': submission.title,
            'score': submission.score,
            'url': submission.url,
            'author': submission.author.name if submission.author else None,
            # 'created_utc': submission.created_utc,
            'comments': comments[:10]
        }
        # print(review)
        reviews.append(review)

    return reviews


def print_topics(movie_title):
    # Use the fetch_movie_reviews function to get movie reviews
    subreddit_name = 'movies'
    reviews = fetch_movie_reviews(subreddit_name, movie_title)
    for review in reviews:
        print(f"Title: {review['title']}")
        print(f"Score: {review['score']}")
        print(f"URL: {review['url']}")
        print(f"Author: {review['author']}")
        if review['comments']:
            first_comment = review['comments'][0]
            second_comment = review['comments'][1]
            print(f"First comment: {first_comment.body}")
            print(f"Second comment: {second_comment.body}")
        else:
            print("No comments found.")

        print('-' * 80)
