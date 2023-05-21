import numpy as np
import pandas as pd
import math
def get_charts(ratings,movies):           #获取排行榜
    movies=set_index(movies)
    movies=movies.iloc[:,:1]
    movies['score']=0
    movies['num']=0
    for row in movies.itertuples():
        frame=get_item_user(ratings,row.Index)
        movies.loc[row.Index,'num']=frame.shape[0]
        movies.loc[row.Index,'score']=frame['rating'].mean()
    movies.sort_values(by=['num'],ascending=False,inplace=True)
    movies.sort_values(by=['score'],ascending=False,inplace=True)
    return movies

def get_user_item(ratings,userId):         #获取用户看过的电影，并按照打分排序
    ratings=ratings[ratings.userId==userId]
    del ratings['userId']
    ratings=ratings.sort_values(by=['rating'],ascending=False,inplace=False)
    return ratings

def get_item_user(ratings,movieId):        #获取看过该电影的用户，并按照打分排序
    ratings=ratings[ratings.movieId==movieId]
    del ratings['movieId']
    ratings.sort_values(by=['rating'],ascending=False,inplace=True)
    return ratings

def set_index(data):                        #将电影Id设置为索引
    data.index=data['movieId']
    del data['movieId']
    return data

def get_genres(movie):                      #获取电影genres
    return movie.iloc[0,2].split('|')