# author: roczhang
# file: demo2_file.py
# time: 2021/04/18
import os

path = "/data/file/pytorch_data/file_path2/"
f = os.listdir(path)
n = 0
for i in f:
    print(i[0:3])
    oldname = path+i
    str_oldname = i[0:3]
    newname = path+str_oldname+str(n)+'.txt'
    os.rename(oldname, newname)
    n += 1
    print(oldname, " ====>", newname)
