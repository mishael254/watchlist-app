import unittest
from .models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    a test class to test the behaviour of the movie class
    '''
    def setUp(self):
        '''
        a setUp method that will run before every test
        '''
        self.new_movie = Movie(1234,'python must be crazy','a thrilling new python series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_init(self):
        '''
        a test case to ensure that objects are instanciated correctly
        '''
        self.assertEqual(self.new_movie.id,1234)
        self.assertEqual(self.new_movie.title,'python must be crazy')
        self.assertEqual(self.new_movie.overview,'a thrilling new python series')
        self.assertEqual(self.new_movie.poster,'https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average,8.5)
        self.assertEqual(self.new_movie.vote_count,12993)


    def test_instance(self):
            self.assertTrue(isinstance(self.new_movie,Movie))

if __name__ == '__main__':
    unittest.main()