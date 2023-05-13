def get_charts(ratings,movies):
    movies=movies.iloc[:,:2]
    movies['score']=0
    for row in ratings.itertuples():
        id=row.movieId
        rating=row.rating
        movies.loc[id,'score']+=rating
    movies.sort_values(by=['score'],ascending=False,inplace=True)
    return movies

#def get_user_item(ratings,id):
