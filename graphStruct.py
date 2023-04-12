# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/10 18:07
# @File    : graphStruct.py
from cacheFunction import load_cached_movies
import networkx as nx
import plotly.graph_objects as go


def similarity(movie1, movie2):
    genres_similarity = len(set(movie1['genres']) & set(movie2['genres']))
    actors_similarity = len(set(movie1['actors']) & set(movie2['actors']))
    directors_similarity = int(movie1['directors'] == movie2['directors'])

    return genres_similarity + actors_similarity + directors_similarity


def find_similar_movies(movie_data, target_title, top_n=5):
    # print(movie_data)
    target_movie = movie_data[target_title]
    similarities = [(title, similarity(target_movie, movie)) for title, movie in movie_data.items() if
                    title != target_title]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]


def create_similarity_graph(movie_data, similar_movies):
    G = nx.Graph()
    for movie_title, similarity_score in similar_movies:
        G.add_node(movie_title, title=movie_title)
        G.add_edge(movie_data["target_movie"]["title"], movie_title, weight=similarity_score)

    return G


def draw_similarity_graph_plotly(graph, target_title):
    edge_x = []
    edge_y = []
    edge_weights = []
    pos = nx.spring_layout(graph, seed=42)

    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_weights.append(graph[edge[0]][edge[1]]['weight'])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='text',
        text=edge_weights,
        mode='lines')

    node_x = [pos[node][0] for node in graph.nodes()]
    node_y = [pos[node][1] for node in graph.nodes()]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[node for node in graph.nodes()],
        textposition="top center",
        textfont=dict(size=12, color='#888'),
        marker=dict(
            showscale=False,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title=f'Similarity Graph for {target_title}',
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    fig.show()


if __name__ == '__main__':
    pass
    # movie_data = load_cached_movies('movie_data.json')  # Find the top 5 similar movies
    # target_title = "Gladiator"
    # top_similar_movies = find_similar_movies(movie_data, target_title, top_n=5)
    # print(f"Top 5 similar movies to {target_title}:")
    # for title, similarity_score in top_similar_movies:
    #     print(f"{title} (similarity: {similarity_score})")
    #
    # # Create and draw the similarity graph
    # movie_data["target_movie"] = movie_data[target_title]
    # G = create_similarity_graph(movie_data, top_similar_movies)
    # draw_similarity_graph_plotly(G, target_title)
