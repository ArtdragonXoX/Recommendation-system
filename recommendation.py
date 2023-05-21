import numpy as np
import pandas as pd
import load_data as ld


class recommendation(object):
    def __init__(self):
        self.movies=ld.loadMovies()
        self.ratings=ld.loadRatings()
        self.sim=ld.loadSim()
        self.movies=self.set_index(self.movies)

    def get_charts(self):           #获取排行榜
        movies=self.movies
        # movies=self.set_index(movies)
        movies=movies.iloc[:,:1]
        movies['score']=0
        movies['num']=0
        for row in movies.itertuples():
            frame=self.get_item_user(row.Index)
            movies.loc[row.Index,'num']=frame.shape[0]
            movies.loc[row.Index,'score']=frame['rating'].mean()
        movies.sort_values(by=['num'],ascending=False,inplace=True)
        movies.sort_values(by=['score'],ascending=False,inplace=True)
        return movies
    
    def set_index(self,data):                        #将电影Id设置为索引
        data.index=data['movieId']
        del data['movieId']
        return data
    
    def movieId_name(self,movieId):                  #根据电影Id返回电影标题
        movies=self.movies
        # movies=self.set_index(movies)
        print(movies.loc[int(movieId),'title'])
        return movies.loc[int(movieId),'title']

    def get_item_user(self,movieId):        #获取看过该电影的用户，并按照打分排序
        ratings=self.ratings
        ratings=ratings[ratings.movieId==movieId]
        del ratings['movieId']
        ratings.sort_values(by=['rating'],ascending=False,inplace=True)
        return ratings
    
    def get_user_item(self,userId):         #获取用户看过的电影，并按照打分排序
        ratings=self.ratings
        ratings=ratings[ratings.userId==userId]
        del ratings['userId']
        ratings=ratings.sort_values(by=['rating'],ascending=False,inplace=False)
        return ratings
    
    def get_recommend(self,userId):                    #预测该用户对所有电影的偏好度
        userId=int(userId)
        sim_mat=self.sim
        # print(userId)
        user_movies=self.get_user_item(userId)
        # print(user_movies)
        sim_mat.index=sim_mat.movieId
        for row in user_movies.itertuples():
            sim_mat=sim_mat.drop(columns=str(row.movieId),inplace=False)
        num_movies=user_movies.shape[0]
        ratings=np.array(user_movies['rating'])
        column=sim_mat.columns.tolist()
        mat=pd.DataFrame(np.zeros((0,sim_mat.shape[1])))
        mat.columns=sim_mat.columns
        for row in user_movies.itertuples():
            mat=pd.concat((mat,sim_mat.loc[[row.movieId]]),axis=0,join='outer')
        # print(mat)
        frame=pd.DataFrame(np.zeros((sim_mat.shape[1],1)))
        frame.index=column
        for i in column:
            x=np.array(mat[i])
            z=np.dot(ratings,x)/num_movies
            frame.loc[i]=z
        frame=frame.sort_values(by=[0],ascending=False,inplace=False)
        return frame
    

# re=recommendation()
# print(re.get_recommend(1))