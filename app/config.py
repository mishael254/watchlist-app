class Config:
    """
    general configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=7fc17f781f7ad8fa7e2c2c1b211fcfe0'
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