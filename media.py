import webbrowser


class Movie():
    """This class stores movie-related info by taking functions for the titl
       e, storyline, poster image and the youtube trailer, in that order"""
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
