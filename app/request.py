from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

#getting the API key
api_key = app.config['MOVIE_API_KEY']

# getting the movie base url
base_url = app.config['MOVIE_API_BASE_URL']

