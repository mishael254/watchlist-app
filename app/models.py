# movie class

class Movie:
    '''
    a movie class that define movie objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count



#review class
class Review:
    all_reviews = []
    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


        #saving the reviews
    def save_review(self):
        Review.all_reviews.append(self)

        # displaying the reviews
    @classmethod
    def get_reviews(cls,id):
        response = []
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
