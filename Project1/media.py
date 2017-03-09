import webbrowser

class Video():
	""" This class provides a way to store videos related information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title = None, duration = None, video_youtube = None, poster_image = None):
		self.title = title
		self.duration = duration
		self.video_youtube_url = video_youtube
		self.poster_image_url = poster_image


	def show_trailer(self):
		webbrowser.open(self.video_youtube_url)


	def show_info(self):
		print("Video Name: " + self.title)
		print("Video Duration: " + self.duration)
		print("Video Link: " + self.video_youtube_url)



class Movie(Video):
	""" This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
		# self.title = movie_title
		Video.__init__(self, movie_title, movie_duration, trailer_youtube, poster_image)
		self.storyline = movie_storyline



class TvShow(Video):
	""" This class provides a way to store TV show related information"""

	def __init__(self, tv_title, tv_duration, tv_youtube, poster_image, tv_season, tv_episode, tv_station):
		Video.__init__(self, tv_title, tv_duration, tv_youtube, poster_image)
		self.season = tv_season
		self.episode = tv_episode
		self.tv_station = tv_station