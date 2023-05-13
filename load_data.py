import pandas as pd

def loadMovies():
    data=pd.read_csv(r'Data\movies.csv')
    data.index=data['movieId']
    del data['movieId']
    return data

def loadRatings():
    data=pd.read_csv(r'Data\ratings.csv',usecols=[0,1,2])
    return data

def loadTags():
    data= pd.read_csv(r'Data\tags.csv',usecols=[0,1,2])
    return data

