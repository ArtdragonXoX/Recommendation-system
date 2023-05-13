import load_data
import recommendation_algo as ra
movies=load_data.loadMovies()
ratings=load_data.loadRatings()
tags=load_data.loadTags()

print(ra.get_item_user(ratings,1))