from flask import render_template
from app import app
from .request import get_movies

@app.route('/')
def index():
    '''
    a view route page function that returns the index page and its data
    '''
    # getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')



    title = 'welcome to the best web movie review online'
    return render_template('index.html',title = title,popular = popular_movies,upcoming = upcoming_movie,now_showing = now_showing_movie)
@app.route('/movie/<int:movie_id>')
def movie (movie_id):
    '''
    new movie page function that returns the movie details page and its data
    '''
    title = 'movies 2020 '
    return render_template('movie.html', title = title , id = movie_id )
