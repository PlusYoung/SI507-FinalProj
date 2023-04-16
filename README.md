# Personalized Movie Recommendation System using TMDb and Reddit APIs
This project is a movie recommendation system based on the TMDb and Reddit APIs. It can retrieve specific data based on a valid database provided by the user or according to user preferences using the APIs, and present the information in various forms (including: movie details display, recommended movie ratings distribution chart, similar movie recommendations chart, and movie discussion board display）
## Prerequisites
**Libaries:**
* shutil
* time
* pprint
* jsonschema
* json
* praw
* requests
* networkx
* plotly
* anytree

**APIS：**
* TMDb API
    * API_KEY = 'aa81dde10be1a5e7a104fb616de2beca'
    * tip: We can change ‘params’ to get attributes we want
* Reddit API
    * REDDIT_CLIENT_ID = 'OoVKZzqmvk2-dll_XiIjIQ'
    * REDDIT_SECRET = 'PSRIKy3ciYIv_kC1X5JXboN43nBv1A'
    * REDDIT_USER_AGENT = 'reddit:MovieRecommender:v1.0 (by /u/dsdjsdoi)'  
    * tip: The data was accessed using PRAW, a Python wrapper for the Reddit API. Reddit was used to fetch movie reviews from the subreddit 'movies'.

## Running the Program
* Step 1: Execute the main script or command.
* Step 2: Follow the prompts or input commands as needed.
    * Put your own valid json data in same dictionary if you have
    * Give your preference about movies [geners and years]
    * Cache this original json data and name this json file by yourself
    * Cache revised json data and name this file by yourself
    * Use menu to choose the result you want to see
* Step 3: Get the graph output or text results.

## Additional Information
The modified JSON file differs from the originally saved file in that an additional layer of key is added before each movie module, named after the movie title. This makes it easier to retrieve related information for each movie by its title in subsequent data processing. 

The original JSON data will be saved by default in the 'movie_data.json' file, which is provided in the GitHub repository. This file can serve as a template for JSON format obtained from APIs or as a test file for users who want to provide their own data at the beginning. The updated revised JSON data will replace the 'movie_data.json' file by default (input 'None' when prompted for a new name). If you don't want to replace the original file, you can rename it to a different name. I have uploaded 'add_data_layer.json' on GitHub, which stores the revised JSON data. You can refer to this file to understand the format of the revised JSON data.
