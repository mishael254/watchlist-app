from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    a view route page function that returns the index page and its data
    '''
    message = 'hello dickface'
    return render_template('index.html',message = message)
@app.route('/movie/<int:movie_id>')
def movie (movie_id):
    '''
    new movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)
