import webbrowser

class Video():
	""" This class provides a way to store videos related information
		
		Attributes:
			title : The title of video
			duration : The time of duration of the video trailer
			video_youtube : The URL link of video trailer on youtube
			poster_image : The post image of the video trailer

		VALID_RATINGS : There are four choices of valid ratings, namely, G, PG, PG-13, R

		Functions:
			show_trailer() : Open a weblink of video trailer
			show_info()    : Print the infomation of video

	"""

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
	""" This class provides a way to store movie related information

		Attributes:
			movie_title : The title of movie
			movie_duration : The time of duration of the movie trailer
			movie_storyline : A brief introduction of the movie
			poster_image : The post image of the movie trailer
			trailer_youtube : The URL link of movie trailer on youtube


	"""

	def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
		# self.title = movie_title
		Video.__init__(self, movie_title, movie_duration, trailer_youtube, poster_image)
		self.storyline = movie_storyline



class TvShow(Video):
	""" This class provides a way to store TV show related information
		
		Attributes:
			tv_title     : The title of TV
			tv_duration  : The time of duration of the TV trailer
			poster_image : The post image of the TV trailer
			tv_youtube   : The URL link of TV trailer on youtube
			tv_season    : The season of TV
			tv_episode   : The episode link of TV
			tv_station   : The station of TV


	"""

	def __init__(self, tv_title, tv_duration, tv_youtube, poster_image, tv_season, tv_episode, tv_station):
		Video.__init__(self, tv_title, tv_duration, tv_youtube, poster_image)
		self.season = tv_season
		self.episode = tv_episode
		self.tv_station = tv_station