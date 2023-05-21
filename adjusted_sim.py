import numpy as np
import recommendation_algo as ra
import pandas as pd
import math
import csv

class ReAlgo(object):
    def __init__(self,movies,ratings):
        self.movies=movies
        self.ratings=ratings
        np.random.seed(0)
        self.w=np.random.randint(0,5)
        self.b=0

    def get_user_rating_mean(self,userId):          #计算用户的打分均值
        user_list=ra.get_user_item(self.ratings,userId)
        user_list=user_list['rating'].tolist()
        user_list=np.array(user_list)
        return np.mean(user_list)
    
    def get_all_ratings_mean(self):             #获取所有用户的打分均值
        frame=self.ratings.drop_duplicates(subset='userId',keep='first',inplace=False)
        del frame['rating']
        del frame['movieId']
        frame.index=frame['userId']
        frame['mean']=0
        for row in frame.itertuples():
            mean=self.get_user_rating_mean(row.userId)
            frame.loc[row.userId,'mean']=mean
        return frame

    def adjusted_sim(self,x,y):                    #计算两部电影的皮尔逊系数,传入的为电影Id
        users_x_rating=self.ratings[self.ratings.movieId==x]
        users_y_rating=self.ratings[self.ratings.movieId==y]
        users_x=users_x_rating['userId'].tolist()
        users_y=users_y_rating['userId'].tolist()
        users=list(set(users_x)&set(users_y))
        deno=0.0
        mole_x=0.0
        mole_y=0.0
        for i in users:
            this_user_mean=self.mean.loc[i,'mean']
            this_user_rating_x=users_x_rating[users_x_rating['userId']==i].iloc[0,2]
            this_user_rating_y=users_y_rating[users_y_rating['userId']==i].iloc[0,2]
            deno+=(this_user_rating_x-this_user_mean)*(this_user_rating_y-this_user_mean)
            mole_x+=(this_user_rating_x-this_user_mean)**2
            mole_y+=(this_user_rating_y-this_user_mean)**2
        mole_x=math.sqrt(mole_x)
        mole_y=math.sqrt(mole_y)
        if(mole_x==0 or mole_y==0):
            return 0
        return deno/(mole_x*mole_y)

    def get_similarity_matrix(self,user_movies):            #获取用户看过的电影和所有电影的相似度矩阵
        frame=pd.DataFrame(np.zeros((user_movies.shape[0],self.movies.shape[0])))
        frame.index=user_movies['movieId']
        frame.columns=self.movies['movieId']
        column=frame.columns.tolist()

        print(frame)
        return frame
    
    def get_recommend(self,user_movies):                    #预测该用户对所有电影的偏好度
        sim_mat=self.get_similarity_matrix(user_movies)
        for i in user_movies.itertuples():
            del sim_mat[i.movieId]
        num_movies=user_movies.shape[0]
        ratings=np.array(user_movies['rating'])
        column=sim_mat.columns.tolist()
        frame=pd.DataFrame(np.zeros((sim_mat.shape[1],1)))
        frame.index=column
        for i in column:
            x=np.array(sim_mat[i])
            z=np.dot(ratings,x)/num_movies
            frame.loc[i]=z
        return frame

    def get_specific_recommend(self,user_movies,movieId):    #预测该用户对某个电影的偏好度
        num_movies=user_movies.shape[0]
        user_movies.index=user_movies['movieId']
        res=0.0
        for i,_i in user_movies.iterrows():
            res+=(self.adjusted_sim(i,movieId)*user_movies.loc[i,'rating'])
            print(res)
        res/=num_movies
        return res
    
    def get_all_similarity_matrix(self):                    #生成所有电影的相似度矩阵并导出
        self.mean=self.get_all_ratings_mean()
        with open("test3.csv","a",newline='') as csvfile: 
            writer = csv.writer(csvfile)
            # row=['movieId']
            # row.extend(self.movies['movieId'].tolist())
            # print(row)
            # writer.writerow(row)
            frame=pd.DataFrame(np.zeros((self.movies.shape[0],self.movies.shape[0])))
            frame.index=self.movies['movieId']
            frame.drop(frame[frame.index<138208].index,inplace=True)
            frame.columns=self.movies['movieId']

            column=frame.columns.tolist()
            for i,_i in frame.iterrows():
                row=[i]
                for j in column:
                    if i==j:
                        row.append(1.0)
                        continue
                    tem=self.adjusted_sim(i,j)
                    row.append(tem)
                    print(i,"和",j,"的相似度为",tem)
                writer.writerow(row)
            csvfile.close()
