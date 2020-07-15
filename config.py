import os

class Config:
    """
    general configuration parent class
    """
    MOVIE_API_KEY = os.environ.get('8a21c603e77fea3673a707f5e3736e64')
    SECRET_KEY = os.environ.get('12345678910')
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    
class ProdConfig(Config):
    '''
    production configuration child class
    arguments config this is the parent class
    '''
    pass
class DevConfig(Config):
    '''
    development configuration child class
    '''
    pass
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}