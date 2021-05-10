# author: roczhang
# file: demo1_file.py
# time: 2021/04/18

import os
print(os.getcwd())

# 把文件夹的每个文件都保存到了集合里面
f = os.listdir(os.getcwd())
print(f)

os.rename("/data/file/pytorch_data/file_path/1（第 3 个复件）.txt", "/data/file/pytorch_data/file_path/2.txt")

# 批量改名
path = "/data/file/pytorch_data/file_path/"
n = 0
p = 0
f = os.listdir(path)
for i in f:
    oldname = path + f[n]
    newname = path + 'output' + str(p) + '.txt'
    os.rename(oldname, newname)
    print(oldname, " ====>", newname)
    p += 1
    n += 1
