class Config:
    """
    general configuration parent class
    """
    MOVIE_API_KEY = '8a21c603e77fea3673a707f5e3736e64'
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=8a21c603e77fea3673a707f5e3736e64'
    pass
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