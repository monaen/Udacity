import fresh_tomatoes
import media

## Movies

# Inception movie instance
inception = media.Movie(movie_title = "Inception", movie_duration = 30,
						movie_storyline = "A movie in dream",
						poster_image = "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_(2010)_theatrical_poster.jpg",
						trailer_youtube = "https://www.youtube.com/watch?v=66TuSJo4dZM")

# School of Rock movie instance
school_of_rock = media.Movie(movie_title = "School of Rock", movie_duration = 30,
							 movie_storyline = "Using rock music to learn",
							 poster_image = "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 trailer_youtube = "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Ratatouille movie instance
ratatouille = media.Movie(movie_title = "Ratatouille", movie_duration = 30,
						  movie_storyline = "A rat is a chef in Pairs",
						  poster_image = "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						  trailer_youtube = "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Midnight in Paris movie instance
midnight_in_paris = media.Movie(movie_title = "Midnight in Paris", movie_duration = 30,
								movie_storyline = "Going back in time to meet authors",
								poster_image = "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
								trailer_youtube = "https://www.youtube.com/watch?v=BYRWfS2s2v4")

# Hunger Games in Paris movie instance
hunger_games = media.Movie(movie_title = "Hunger Games", movie_duration = 30,
						   movie_storyline = "A really real reality show",
						   poster_image = "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
						   trailer_youtube = "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Resident Evil in Paris movie instance
resident_evil = media.Movie(movie_title = "Resident Evil 7", movie_duration = 30,
							movie_storyline = "A survival horror movie",
							poster_image = "https://s-media-cache-ak0.pinimg.com/originals/5e/87/ba/5e87baf2dee6a4edd4cca0de65f9e1fd.jpg",
							trailer_youtube = "https://www.youtube.com/watch?v=jbtmW3ydOkU")

# Suicide Squad in Paris movie instance
suicide_squad = media.Movie(movie_title = "Suicide Squad", movie_duration = 30,
							movie_storyline = "An American superhero film",
							poster_image = "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_(film)_Poster.png",
							trailer_youtube = "https://www.youtube.com/watch?v=mMb-RrhTxIE")

# Movie instances list
movies = [resident_evil, suicide_squad, inception, 
		  school_of_rock, ratatouille, midnight_in_paris, 
		  hunger_games]




# TV shows

# Friends tv instance
friends = media.TvShow(tv_title = "Friends",
					   tv_duration = 30,
					   tv_youtube = "https://www.youtube.com/watch?v=lWqUX_aCKBE&list=PL4VjYMnxdYuVdqqAuuURtNHY5cfNFy606&index=2",
					   poster_image = "https://www.warnerbros.com/sites/default/files/friends_completeseries_keyart.jpg",
					   tv_season = 7,
					   tv_episode = "https://www.youtube.com/watch?v=8mP5xOg7ijs",
					   tv_station = "TBS")

# Shield tv instance
shield = media.TvShow(tv_title = "Shield",
					  tv_duration = 30,
					  tv_youtube = "https://www.youtube.com/watch?v=GlQu03jNhk0",
					  poster_image = "http://pre01.deviantart.net/7b3e/th/pre/i/2015/223/0/0/agents_of_shield_season_3_poster_by_malshania-d957z36.jpg",
					  tv_season = 3,
					  tv_episode = "https://www.youtube.com/watch?v=T3T-evQZiQo",
					  tv_station = "Marvel")
# TVs list
tvs = [friends, shield]

# Generate the website !
fresh_tomatoes.open_movies_page(movies + tvs)