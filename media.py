import webbrowser
class Movie():
	""" This class provides a way to store movie related info"""
	def __init__(self, movie_title, storyline, poster_image, trailer_youtube): 
		self.title = movie_title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
