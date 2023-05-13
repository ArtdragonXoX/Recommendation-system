def get_charts(ratings,movies):
    movies=movies.iloc[:,:2]
    movies['score']=0
    for row in ratings.itertuples():
        id=row.movieId
        rating=row.rating
        movies.loc[id,'score']+=rating
    movies.sort_values(by=['score'],ascending=False,inplace=True)
    return movies

def get_user_item(ratings,id):
    ratings=ratings[ratings.userId==id]
    del ratings['userId']
    ratings.sort_values(by=['rating'],ascending=False,inplace=True)
    return ratings

def get_item_user(ratings,id):
    ratings=ratings[ratings.movieId==id]
    del ratings['movieId']
    ratings.sort_values(by=['rating'],ascending=False,inplace=True)
    return ratings