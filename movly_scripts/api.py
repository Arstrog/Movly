import os
import sys
import requests
import movly_scripts.conf as conf


def fetch_movie_data(type):
    types = {
        "playing":"/movie/now_playing",
        "popular":"/movie/popular",
        "top":"/movie/top_rated",
        "upcoming":"/movie/upcoming"
    }
    if type not in types:
        raise ValueError(f"Unknown Category: {type}")
    choice = types.get(type)

    url = f"{conf.BASE_URL}{choice}"

    query_param ={"language":"en-US","page":1}

    try:
        api_response = requests.get(url,headers=conf.HEADERS,params=query_param)
        api_response.raise_for_status()
        data = api_response.json()
        return data.get("results",[])
    except requests.RequestException as err:
        print(f"Api Error occured: {err}")
        return []
