# author: roczhang
# file: demo2_file.py
# time: 2021/04/18
import os

path = "/data/file/rice_frame/MVI_6/"


f = os.listdir(path)
num = 387
for i in f:
    oldname = path + i
    print('oldname:', oldname)
    newname = path + str(num) + '.jpg'
    print('newname:', newname)
    os.rename(oldname, newname)
    num += 1
