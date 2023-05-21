import pandas as pd

def loadMovies():
    data=pd.read_csv(r'Data\movies.csv')
    return data

def loadRatings():
    data=pd.read_csv(r'Data\ratings.csv',usecols=[0,1,2])
    return data

def loadTags():
    data= pd.read_csv(r'Data\tags.csv',usecols=[0,1,2])
    return data

def loadSim():
    data=pd.read_csv(r'Data\all_adjusted_sim.csv')
    return data
