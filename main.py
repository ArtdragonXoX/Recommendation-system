import load_data
import recommendation_algo as ra
movies=load_data.loadMovies()
ratings=load_data.loadRatings()
tags=load_data.loadTags()
charts=ra.get_charts(ratings,movies)
print(charts)