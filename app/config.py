class Config:
    """
    general configuration parent class
    """
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