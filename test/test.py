import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,2,3,3],[8,1,3,8]])
print(np.argmax(a[0,:],axis=0))
print(np.random.randint(a.shape[0], size=3))



'''
#怎么从当下目录的下一级找到合乎要求的文件
'''
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import os

'''
cwd  = os.getcwd()
path = cwd + "/images/cats"
valid_exts = [".jpg",".gif",".png",".tga", ".jpeg"]
imgs = []
names = []
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_exts:
        continue
    fullpath = os.path.join(path,f)
    imgs.append(imread(fullpath))
    names.append(os.path.splitext(f)[0]+os.path.splitext(f)[1])

'''


'''
#Time_Transfer()
# 从一堆数据中找出随机的几个进行处理实例！
# 注意排序和 np.sort()
# 注意zip怎么用的
# time_deviation = 8 * 60 * 60
'''


'''
nimgs = len(imgs)
randidx = np.sort(np.random.randint(nimgs, size=3))
for curr_img, curr_name, i \
        in zip([imgs[j] for j in randidx]
    , [names[j] for j in randidx], randidx):
    plt.figure()
    plt.imshow(curr_img)
    plt.title("[" + str(i) + "] ")
    plt.draw()
'''
