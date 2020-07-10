from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    a view route page function that returns the index page and its data
    '''
    title = 'welcome to the best web movie review online'
    return render_template('index.html',title = title)
@app.route('/movie/<int:movie_id>')
def movie (movie_id):
    '''
    new movie page function that returns the movie details page and its data
    '''
    title = 'movies 2020 '
    return render_template('movie.html', title = title , id = movie_id )
