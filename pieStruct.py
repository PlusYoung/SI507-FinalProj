# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/10 17:05
# @File    : pieStruct.py

import plotly.graph_objs as go
import plotly.subplots as sp

from cacheFunction import load_cached_movies
from treeStruct import tree_from_given_title


def pie_rating(data):
    # Collect vote averages
    vote_averages = [movie["vote average"] for movie in data.values()]

    # Define categories for vote averages
    categories = {
        "0-1": 0,
        "1-2": 0,
        "2-3": 0,
        "3-4": 0,
        "4-5": 0,
        "5-6": 0,
        "6-7": 0,
        "7-8": 0,
        "8-9": 0,
        "9-10": 0,
    }

    # Count the vote averages for each category
    for vote_average in vote_averages:
        for category, upper_bound in zip(categories.keys(), range(1, 11)):
            if vote_average <= upper_bound:
                categories[category] += 1
                break

    # Generate the pie chart
    labels = list(categories.keys())
    sizes = list(categories.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
    fig.update_layout(title_text="Distribution of Vote Averages", legend_title="Vote Average Ranges")
    fig.show()


if __name__ == '__main__':
    data = load_cached_movies("movie_data.json")
    # new_data = tree_from_given_title(data.keys(), data)
    pie_rating(data)
