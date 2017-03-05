import fresh_tomatoes
import media

# toy_story = media.Movie("Toy Story",
# 						"A story of a boy and his toys that come to life",
# 						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
# 						"https://www.youtube.com/watch?v=vwyZH85NQC4")
# # print(toy_story.storyline)
# avatar = media.Movie("Avatar",
# 					 "A marine on an alien planet",
# 					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
# 					 "https://www.youtube.com/watch?v=KYk0zVOAOgQ")
# print(avatar.storyline)
inception = media.Movie("Inception", 30,
						"A movie in dream",
						"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_(2010)_theatrical_poster.jpg",
						"https://www.youtube.com/watch?v=66TuSJo4dZM")
# inception.show_trailer()
school_of_rock = media.Movie("School of Rock", 30,
							 "Using rock music to learn",
							 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", 30,
						  "A rat is a chef in Pairs",
						  "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						  "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "30",
								"Going back in time to meet authors",
								"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
								"https://www.youtube.com/watch?v=BYRWfS2s2v4")
hunger_games = media.Movie("Hunger Games", 30,
						   "A really real reality show",
						   "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
						   "https://www.youtube.com/watch?v=PbA63a7H0bo")
resident_evil = media.Movie("Resident Evil 7", 30,
							"A survival horror movie",
							"http://cdn1-www.comingsoon.net/assets/uploads/gallery/resident-evil-the-final-chapter/last-resident-evil-poster.jpg",
							"https://www.youtube.com/watch?v=jbtmW3ydOkU")
suicide_squad = media.Movie("Suicide Squad", 30,
							"An American superhero film",
							"https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_(film)_Poster.png",
							"https://www.youtube.com/watch?v=mMb-RrhTxIE")

movies = [resident_evil, suicide_squad, inception, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print resident_evil.VALID_RATINGS

friends = media.TvShow(tv_title = "Friends",
					   tv_duration = 30,
					   tv_youtube = "https://www.youtube.com/watch?v=lWqUX_aCKBE&list=PL4VjYMnxdYuVdqqAuuURtNHY5cfNFy606&index=2",
					   poster_image = "https://www.warnerbros.com/sites/default/files/friends_completeseries_keyart.jpg",
					   tv_season = 7,
					   tv_episode = "https://www.youtube.com/watch?v=8mP5xOg7ijs",
					   tv_station = "TBS")
# friends.show_trailer()
shield = media.TvShow(tv_title = "Shield",
					  tv_duration = 30,
					  tv_youtube = "https://www.youtube.com/watch?v=GlQu03jNhk0",
					  poster_image = "http://pre01.deviantart.net/7b3e/th/pre/i/2015/223/0/0/agents_of_shield_season_3_poster_by_malshania-d957z36.jpg",
					  tv_season = 3,
					  tv_episode = "https://www.youtube.com/watch?v=T3T-evQZiQo",
					  tv_station = "Marvel")
tvs = [friends, shield]

# print movies + tvs

fresh_tomatoes.open_movies_page(movies + tvs)