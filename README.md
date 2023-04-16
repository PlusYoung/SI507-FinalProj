# Personalized Movie Recommendation System using TMDb and Reddit APIs
This project is a movie recommendation system based on the TMDb and Reddit APIs in Pythjon. It can retrieve specific data based on a valid database provided by the user or according to user preferences using the APIs, and present the information in various forms (including: movie details tree display, recommended movie ratings distribution pie charts, similar movie recommendations graphes, and movie discussion board display）
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
 Modify **config.py** —— Provide APIs, the template is as follows:
 
 ```python
 # Reddit APIs
   REDDIT_CLIENT_ID = 'client id'
   REDDIT_SECRET = 'secret'
   REDDIT_USER_AGENT = 'user agent'
 # TMDb API
   TMDb_API_KEY = 'key'
 ```
 *tip:I will upload a documentation file named **final_submit_yyanga.pdf** on Canvas, which will include the API I used. Teaching assistants or grading teachers can directly use my API for convenient code execution.*
 

 **To obtain an API key from TMDb by yourself (The Movie Database), follow these steps:**
   * Create an account or sign in: Visit the TMDb website (https://www.themoviedb.org/) and either sign up for a new account or sign in to your existing account.
   * Request an API key: Once you are signed in, go to your account settings by clicking on your avatar in the top right corner and selecting "Settings" from the dropdown menu. Navigate to the "API" tab on the left sidebar.
   * Fill out the application form: Click on "Generate a new API key" and fill out the application form. Choose the type of API key you need (Developer or Professional). For most cases, the Developer option should be sufficient. Provide the required details, such as the application's name, purpose, and a brief description.
   * Accept the terms of use: Review and accept the TMDb API terms of use.
   * Receive your API key: Once your application is submitted, you will receive your API key. It will also be available in your account's API settings.

**To obtain an API key from Reddit (a Client ID, Client Secret and User-Agent string), follow these steps:**
   * Create an account or sign in: Visit the Reddit website (https://www.reddit.com/) and either sign up for a new account or sign in to your existing account.
   * Go to the App Preferences page: Once you are signed in, go to the "App Preferences" page by clicking on your username in the top right corner and selecting "User Settings" from the dropdown menu. Then, navigate to the "Privacy & Security" tab and scroll down to the "App Authorization" section. Click on the "Developed Applications" tab and then click on the "Create App" or "Create Another App" button.
   * Fill out the application form: Provide the necessary information, such as the application's name, description, and redirect URI. Choose the "script" option for the "App type" field. The redirect URI can be set to "http://localhost:8080" if you are using the API for local development.
   * Create the application: Click on the "Create app" button at the bottom of the form to submit your application.
   * Get your Client ID and Client Secret: After successfully creating the application, you will be provided with a "Client ID" and "Client Secret". The Client ID can be found under the application's name in the "Developed Applications" section, and the Client Secret is listed as "secret" in the application's details.
   * Finally create a User-Agent string for 'REDDIT_USER_AGENT': The User-Agent string is a custom text that helps identify your application to the Reddit API. It should follow the format <platform>:<app ID>:<version string> (by /u/<your Reddit username>). For example: python:my-reddit-app:v1.0 (by /u/exampleUser).

## Data Structure
### Tree
 In this project, we utilize a tree data structure to display the detailed information of a movie. The tree is constructed based on a revised JSON file. By calling the `anytree` library, we can directly display the tree structure of the JSON file.

The tree implementation in this project includes the following features:

- Displaying movie details hierarchically
- Visualizing the JSON file as a tree structure

### Graph
  In this project, association graphs are used to show the top five most similar movies by calling the `networkx`. This similarity is calculated based on shared genres, directors, and the number of actors.

The graphs implementation in this project includes the following features: 
 
- Use graph to show the top five most similar movies. 
- The similarity is calculated based on shared genres, directors, and the number of actors. By visualizing the similarities, users can easily identify movies with similar characteristics.
 
## Running the Program
* Step 1: Execute the main script or command.
* Step 2: Follow the prompts or input commands as needed.
   * Put your own valid json data in same dictionary if you have
    
   *tip: your own valid json data should satisfy this json style (You can also use movie_data.json I provided on github to do test):*
    
   ```python
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
    "additionalProperties": False}
   ```
    * Give your preference about movies [geners and years]
    * Cache this original json data and name this json file by yourself
    * Cache revised json data and name this file by yourself
    * Use menu to choose the result you want to see
   
* Step 3: Get the graph output or text results.

## Additional Information
The modified JSON file differs from the originally saved file in that an additional layer of key is added before each movie module, named as the movie title. This makes it easier to retrieve related information for each movie by its title in subsequent data processing. 

The original JSON data will be saved by default in the 'movie_data.json' file, which is provided in the GitHub repository. This file can serve as a template for JSON format obtained from APIs or as a test file for users who want to provide their own data at the beginning. The updated revised JSON data will replace the 'movie_data.json' file by default (input 'None' when the system ask for a new name). If you don't want to replace the original file, you can rename it to a different name. I have uploaded 'add_data_layer.json' on GitHub, which stores the revised JSON data. You can refer to this file to understand the format of the revised JSON data.
