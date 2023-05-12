import LoadData
import RecommendationAlgo as ra
movies=LoadData.loadMovies()
ratings=LoadData.loadRatings()
tags=LoadData.loadTags()
charts=ra.Charts(ratings,movies)
print(charts)