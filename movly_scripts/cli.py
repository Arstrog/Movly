import argparse
import sys
import movly_scripts.api as api

CATEGORY_TYPES=[
    "playing",
    "popular",
    "top",
    "upcoming"
]
def process_now(movies:list):

    sorted_movies = sorted(movies,key=lambda x:x.get("release_date",""),reverse=True )
    return [f"~Title:{m["title"]} \n RealeaseDate: {m["release_date"]} \n" for m in sorted_movies]

def process_pop(movies:list):

    sorted_movies = sorted(movies,key=lambda x:x.get("popularity",""),reverse=True )
    return [f"~Title:{m["title"]} \n PopularityScore: {m["popularity"]} \n" for m in sorted_movies]

def process_top(movies:list):

    sorted_movies = sorted(movies,key=lambda x:x.get("vote_average",""),reverse=True )
    return [f"~Title:{m["title"]} \n VoteAverage: {m["vote_average"]} \n VoteCount: {m["vote_count"]} \n" for m in sorted_movies]

def process_upcoming(movies:list):

    sorted_movies = sorted(movies,key=lambda x:x.get("release_date",""),reverse=True )
    return [f"~Title:{m["title"]} \n RealeaseDate: {m["release_date"]} \n" for m in sorted_movies]

def display_data(args,data:list):
    cat =  str(args.type) if args.type is not None else sys.exit("Argument was expected.")
    if cat not in CATEGORY_TYPES:
        sys.exit("Incorrect type for processing movie data.")

    funcs = {
        "playing": process_now,
        "popular":process_pop,
        "top":process_top,
        "upcoming":process_upcoming
    }

    process_func = funcs.get(cat)
    if process_func is None:
        raise Exception(f"Method {process_func} is not implemented")
    res = process_func(data)

    for m in res:
        print(m)


def parser()-> argparse.ArgumentParser:
    my_parser = argparse.ArgumentParser(prog="movly",description="Movly is a cli tool used for displaying movie information with the usage of TMDB API.")

    my_parser.add_argument("--type",
        type=str,
        nargs="?",
        choices=CATEGORY_TYPES,
        help="Get the movie results based on the category provided.",
        required=True)
    my_parser.set_defaults(func=display_data)


    return my_parser



def main():
    app_parser = parser()
    args = app_parser.parse_args()
    if args.type not in CATEGORY_TYPES:
        raise ValueError("Lathos edw")
    database = api.fetch_movie_data(args.type)
    args.func(args,database)


if __name__ == "__main__":
    sys.exit(main())
