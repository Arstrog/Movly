import os
from dotenv import load_dotenv


load_dotenv()

BASE_URL = "https://api.themoviedb.org/3"
ACCESS_TOKEN = os.getenv("TMBD_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("Access Token is missing from your .env file.")

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"}
