
import pandas as pd
from math import log
from anytree import Node, RenderTree

'''
# 
# 用来模拟随机深林算法的树是怎么生成的      
#   
# root_node = Node('root')
# curr_node = Node('a-b', parent=root_node)
# curr_node = Node('b-e', parent=curr_node)
# curr_node = Node('a-c', parent=root_node)
# curr_node = Node('a-d', parent=root_node)
# 
# for pre, fill, node in RenderTree(root_node):
#     print("%s%s" % (pre, node.name))

'''

class iterative():

    def  __init__(self,df,tar_column):

        probs = df.groupby(tar_column).size().div(len(df))
        self.h = 0
        for i in probs:
            self.h += -i * log(i , 2)
        self.df = df
        self.tar_column = tar_column
        self.length = len(df)

    def get_one_column_gain(self, df, column):

        one_probs = self.df.groupby(column).size().div(self.length)
        h = 0
        for (index,value) in one_probs.iteritems():
            part_df = df[df[column] == index]
            temp_probs = part_df.groupby(self.tar_column).size().div(len(part_df))

            for i in temp_probs:
                h += -i * log(i , 2) * value
        return h

    def get_max_entropy_gain(self, df):

        d = {}
        for  column in filter(lambda v: v!=self.tar_column, df.columns):
            one_gain = self.get_one_column_gain(df, column)
            d[column] = self.h - one_gain
        return max(d, key=d.get)

    def train_decision_tree(self, df , node):

        c = self.get_max_entropy_gain(df)

        for v in pd.unique(df[c]):
            df_v = df[df[c] == v]
            current_node = Node("%s-%s"%(c,v),parent=node)
            gb = df_v.groupby(self.tar_column)
            #目标中元素个数最多的值
            m = gb.size().idxmax()

            #属性没有用完 且分区纯度非100%
            if len(df_v.columns) > 2 and len(gb) > 1:
                self.train_decision_tree(df_v.drop(c, axis=1) , current_node)
            else:
                Node(m , parent=current_node)


df = pd.read_csv("./../data/test.csv")
root_node = Node('root')
a = iterative(df,"buys_computer")
a.train_decision_tree(df , root_node)
for pre, fill, node in RenderTree(root_node):
    print("%s%s" % (pre, node.name))

