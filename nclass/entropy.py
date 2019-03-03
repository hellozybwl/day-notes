import pandas as pd
import numpy as np
from math import log

'''
# h_value()
#      函数主要功能是求取某个概率的嫡值
#inverse_h()
#      根据嫡值反求函数的概率
'''

class Entropy:

    def __init__(self):
        pass

    def h_value(self, x):
        if x<=0.0 or x>=1:
            return 0
        di = -x*log(x,2) - (1-x)*log((1-x),2)
        return di

    def inverse_h(self,value, x_start = 0.0001, x_end = 0.5 ,error = 1e-4):
        if value <= 0.0 or value >=1.0:
            return 0
        golden_point_param = 0.68
        x_continue = x_start + (x_end - x_start) * golden_point_param
        new_value = self.h_value(x_continue)
        while abs(new_value - value) > error :
            if new_value > value:
                x_end = x_continue
                x_continue = x_end - (x_end - x_start) * golden_point_param
            else:
                x_start = x_continue
                x_continue = x_start + (x_end - x_start) * golden_point_param
            new_value = self.h_value(x_continue)
        return x_continue


'''
#WriteCsvFile()
#      怎样写csv文件
'''

'''
# columns = ['x1','x2', 'x3', 'x4']
# csv_instance = WriteCsvFile("train.csv",columns)
# 
# data = {}
# x_matix =  np.random.random((12,4))
# a_matix = 10 * np.random.random((4,1))
# random_matix = 3 * np.random.random((12,1))
# 
# for i in range(len(columns)):
#     data[columns[i]] = x_matix[:,i]
# 
# no_noise_y = np.dot(x_matix , a_matix)
# noise_y = no_noise_y + random_matix
# 
# data['no_noise_y'] = np.array([value[0] for value in no_noise_y])
# data['noise_y'] = np.array([value[0] for value in noise_y])
# 
# csv_instance.write_csv(data)
'''

class WriteCsvFile():
    def __init__(self,file_name,columns_array):
        self.file = file_name
        self.column = columns

    def write_csv(self,data):
        pd_data = pd.DataFrame(data)
        pd_data.to_csv(self.file, index=False)



'''
#WriteCsvFile()
#      求最小方差类

# Y1 = np.array([[10],[25],[6],[7],[6],[16]])
# Y2 = np.array([[14],[12],[3],[9],[3],[15]])
# X1 = np.array([[-2,-1,0,1,2],[-1,0,1,2,3],[1,1,1,0,0],[1,1,0,1,0],[1,0,0,0,1],[1,1,1,1,1]])
# X2 = np.array([[1,0,0,2,1],[-1,0,2,1,1],[-3,1,2,0,0],[-4,2,0,1,1],[1,1,0,0,0],[1,1,1,1,1]])
# X = np.vstack((X1,X2))
# Y = np.vstack((Y1,Y2))
#
# least_instance = Least_square()
# param = least_instance.fit(X,Y)
# print(param)
# result,var = least_instance.predict(X)
# print(result)
# print(var)
'''

class Least_square:
    def __init__(self):
        self.param = np.array([])
        self.Y = np.array([])

    def fit(self, X, Y):
        X_T = X.transpose()
        self.param = np.dot(np.dot(np.linalg.inv(np.dot(X_T,X)),X_T),Y)
        self.Y = Y
        return self.param

    def predict(self,X):
        result = np.dot(X,self.param)
        var = np.var(self.Y - result)
        return result, var


'''
#Time_Transfer()
# 时间转换的类
#以一个小时的时间为采样周期，并对所以时间做以下处理
#一天多少秒
# day_seconds= 24 * 60 * 60
#Unix时间戳 0 代表1970/1/1 8:0:0
# time_deviation = 8 * 60 * 60
	
'''

class Time_Transfer():
    #两个时间转换的函数
    def tmStampToTmStr(tmStamp):
        tmObject = time.localtime(tmStamp)
        tmStr = time.strftime("%Y-%m-%d %H:%M:%S", tmObject)
        return tmStr

    def tmStrToTmStamp(tmStr):
        if len(tmStr) == 10:
            tmStr = tmStr + " " + "00:00:00"
        formatStr = "%Y-%m-%d %H:%M:%S"
        tmObject = time.strptime(tmStr, formatStr)
        tmStamp = time.mktime(tmObject)
        return int(tmStamp)

