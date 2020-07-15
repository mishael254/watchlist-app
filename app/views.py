from flask import render_template
from app import app
from .request import get_movies
from .request import get_movies,get_movie
from .request import get_movies,get_movie,search_movie
from flask import render_template,request,redirect,url_for

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

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('index.html',title = title,popular = popular_movies,upcoming = upcoming_movie,now_showing = now_showing_movie)
@app.route('/movie/<int:id>')
def movie (id):
    '''
    new movie page function that returns the movie details page and its data
    '''
    
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title , movie = movie )
# searching movies
@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    view function to display search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', movies = searched_movies, title = title)