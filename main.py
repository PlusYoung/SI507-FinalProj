import shutil
import time
from pprint import pprint

import constant
from dataReddit import print_topics
from dataTMDb import fetch_movies_more
from cacheFunction import load_cached_movies, add_one_layer_to_json, cache_data_to_json
from checkInput import start_input, self_input, choice_input, detail_input
from jsonschema import validate, ValidationError

from graphStruct import find_similar_movies, create_similarity_graph, draw_similarity_graph_plotly
from pieStruct import pie_rating
from treeStruct import print_tree


def main():
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    print("Welcome to 'Movie Recommendation System'!")
    flag = input("Do you already have your own valid json database(Y/N)? [If this is the first time you use this "
                 "system, please answer 'N']: ")
    yes_list = ['y', 'yes', 'yup', 'yea']
    no_list = ['n', 'no', 'nope', 'nah']
    while True:
        if flag in yes_list:
            path = self_input("Make sure your json file is in your program dictionary and please enter your filename:"
                              "(e.g. data.json) ")
            # load data you already have
            movie_data = load_cached_movies(path)
            try:
                # justify the json data is valid
                [validate(movie_data[i], constant.schema) for i in range(len(movie_data))]
                break
            except ValidationError as e:
                print("JSON database is not valid. The invalid messages are:", e.message)
                flag = input(
                    "Do you already have another your own valid json database(Y/N)? :")
            except TypeError as e:
                flag = input(
                    "Do you already have another your own valid json database(Y/N)? :")
        elif flag in no_list:
            print()
            print("*" * width)
            print("OK! That's fine! Let us provide database for you! Give us your preference!!")
            print("*" * width)
            print()
            print("Here is the movie genre codes. ")
            pprint(constant.genre_id_to_name)
            genre_ids = start_input(constant.genre_id_to_name)
            years = start_input(constant.year_can_be_get)
            # cache data to json
            chose = input(
                "Do you want each selected movie to belong to every genre you preferred above, or is it sufficient "
                "for a movie to belong to just one of those genres? (1/2): ")
            while True:
                if int(chose) == 1:
                    break
                elif int(chose) == 2:
                    break
                else:
                    chose = input("Your input is invalid! Please Enter again: ")
            movie_data, path = fetch_movies_more(years, genre_ids=genre_ids, flag=int(chose))
            break
        else:
            flag = input("Your input is invalid! Please Enter again: ")
    # add the 'title' to each json dict module, which will make the json module easily read by movie title
    movie_data_final = add_one_layer_to_json(movie_data)
    add_layer_path = self_input(
        "The final recommend data will be saved to a JSON file for further processing. "
        "please enter the new file name: ")
    cache_data_to_json(add_layer_path, movie_data_final)
    # print(movie_data_final)
    while True:
        print()
        print("*" * width)
        print("Here is the overall recommended movie names based on your preference! Or the database you provided!", '\n')
        print(movie_data_final.keys(), '\n')
        print("*" * width)
        print("You can use the menu to do your choice!")
        print("1. See more details about the movie you chosen from the overall recommendation.")
        print("2. View the rating distribution of recommended movies.[0-10]")
        print("3. Find similar movies more accurately. (Deeply recommendation)")
        print("4. View related topics or discussion of a certain movie.")
        print("5. Exit!")

        your_choice = choice_input("Input your choice: ")
        if your_choice == '1':
            detail_need_movie = detail_input("Print the name of movie(s) you want to see its details[use comma to "
                                             "separate movies] (e.g. Britannic,The Crossing,Vola sciusciù): ",
                                             movie_data_final)
            print()
            print("Here is the detailed information represented by tree-structure.")
            print("-" * width)
            print_tree(detail_need_movie, movie_data_final)
            time.sleep(3)

        elif your_choice == '2':
            data_rating = load_cached_movies(add_layer_path)
            pie_rating(data_rating)

        elif your_choice == '3':
            # print(movie_data)
            target_title = detail_input("Please provide the title of your favorite movie from the recommended list. "
                                         "We will find the top 5 most similar movies based on genre and actor "
                                         "similarities for the given title:", movie_data_final)[0]
            top_similar_movies = find_similar_movies(movie_data_final, target_title, top_n=5)
            print(f"Top 5 similar movies to {target_title}:")
            for title, similarity_score in top_similar_movies:
                print(f"{title} (similarity: {similarity_score})")
            # Create and draw the similarity graph
            movie_data_final["target_movie"] = movie_data_final[target_title]
            G = create_similarity_graph(movie_data_final, top_similar_movies)
            draw_similarity_graph_plotly(G, target_title)

        elif your_choice == '4':
            movie_topics = detail_input("Print the name of movie you want to view related topics or discussion: ",
                                        movie_data_final)
            print_topics(movie_topics)
        else:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    # Load cached movies from the JSON file
    # movie_cache = load_cached_movies('movie_data.json')
    # if movie_cache:
    #     print(json.dumps(movie_cache, indent=4))
    # else:
    #     print("No cached movies found.")
