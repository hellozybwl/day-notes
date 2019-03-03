import unittest
from nclass.entropy import *
import pandas as pd
import numpy as np
from data.config import *


class TestMathFunc(unittest.TestCase):

    def test_entropy(self):
        y = Entropy().h_value(0.08333)
        x = Entropy().inverse_h(0.5)
        print(x, y)

    def test_read_csv(self):
        file = root_path + 'data/test.csv'
        df = pd.read_csv(file)
        for (i,v) in enumerate(pd.unique(df['age'])):
            if i != len(pd.unique(df['age'])) :
                print(v)

    def test_least_squares(self):

        Y1 = np.array([[10],[25],[6],[7],[6],[16]])
        Y2 = np.array([[14],[12],[3],[9],[3],[15]])
        X1 = np.array([[-2,-1,0,1,2],[-1,0,1,2,3],[1,1,1,0,0],[1,1,0,1,0],[1,0,0,0,1],[1,1,1,1,1]])
        X2 = np.array([[1,0,0,2,1],[-1,0,2,1,1],[-3,1,2,0,0],[-4,2,0,1,1],[1,1,0,0,0],[1,1,1,1,1]])
        X = np.vstack((X1,X2))
        Y = np.vstack((Y1,Y2))

        least_instance = Least_square()
        param = least_instance.fit(X,Y)
        result,var = least_instance.predict(X)
        print(param)

    def test_write_csv(self):

        data = {}
        columns = ['x1','x2', 'x3', 'x4']

        x_matix =  np.random.random((12,4))
        a_matix = 10 * np.random.random((4,1))

        for i,value in enumerate(columns):
            data[value] = x_matix[:,i]

        no_noise_y = np.dot(x_matix , a_matix)
        data['no_noise_y'] = no_noise_y.T.tolist()[0]

        # pd_data = pd.DataFrame(data)
        # pd_data.to_csv("train.csv", index=False)



    def test_dfarray_operater(self):

        df = pd.DataFrame({'col1': [0, 3, 2, 3], 'col2': [4, 0, 2, 1]},
                          index=['a', 'b', 'c', 'd'])
        print(df)
        # print(df['col1'])
        # print(type(df['col1']))
        # print(df['col1'].max())
        # print(df.max(axis=1))
        # print(df.max())
        # print(type(df.max()))
        # print(df['col1'].idxmax())
        # print("*"*30)
        # print(df['col1'][df['col1'] == df['col1'].max()])
        # print("*"*30)
        # print(df['col1'][df['col1'] == df['col1'].max()].index)
        # print("*"*30)
        # print(df['col1'][df['col1'] == df['col1'].max()].index.values)
        # print(list(df['col1'][df['col1'] == df['col1'].max()].index))
        # print(df['col1'][df['col1'] == df['col1'].min()].index.values)
        # print(df.loc['a'].idxmax())


    def test_save_svgimg(self):

        import pygal
        from math import cos

        xy_chart = pygal.XY()
        xy_chart.title = 'XY Cosinus'
        xy_chart.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
        xy_chart.add('y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
        xy_chart.add('x = 1',  [(1, -5), (1, 5)])
        xy_chart.add('x = -1', [(-1, -5), (-1, 5)])
        xy_chart.add('y = 1',  [(-5, 1), (5, 1)])
        xy_chart.add('y = -1', [(-5, -1), (5, -1)])
        svg_file = root_path + "/img/xyline.svg"
        xy_chart.render_to_file(svg_file)

        # bar_chart = pygal.Bar()
        # bar_chart.add('Fibonacci',[0,1,1,2,3,5,8,13,21,34,55])
        # bar_chart.render_to_file('Hello.svg')



if __name__ == '__main__':




    #logger.info("begin")

    #如果要全部测试，就用这句话
    unittest.main()

    #如果只测试1个例子，请用下面的程序
    #suite = unittest.TestSuite()
    # suite.addTest(TestMathFunc('test_entropy'))
    # unittest.TextTestRunner(verbosity=2).run(suite)



