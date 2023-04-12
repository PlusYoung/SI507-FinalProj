# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/9 13:35
# @File    : constant.py

genre_id_to_name = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western'
}

year_can_be_get = [str(i) for i in range(2000, 2023)]

# Define JSON schema
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "year": {"type": "string", "pattern": "^\\d{4}$"},
        "genres": {
            "type": "array",
            "items": {"type": "string"}
        },
        "actors": {
            "type": "array",
            "items": {"type": "string"}
        },
        "directors": {"type": "string"},
        "overview": {"type": "string"},
        "popularity": {"type": "number"},
        "vote average": {"type": "number"},
        "vote count": {"type": "integer"}
    },
    "required": [
        "id",
        "title",
        "year",
        "genres",
        "actors",
        "directors",
        "overview",
        "popularity",
        "vote average",
        "vote count"
    ],
    "additionalProperties": False
}
