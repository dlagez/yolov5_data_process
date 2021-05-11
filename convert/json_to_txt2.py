# author: roczhang
# file: json_to_txt.py
# time: 2021/05/11
import json
import os

# 将json文件夹转换成txt（yolo格式）
json_dir = '/data/file/yolo5/json/'
json_files = os.listdir(json_dir)

txt_dir = '/data/file/yolo5/txt/'
if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

for json_file in json_files:
    # json_file = '1.json'
    txt_name = json_file.split('.')[0] + '.txt'
    # print(txt_name)
    txt_file = open(os.path.join(txt_dir, txt_name), 'w')

    def convert(minc, minr, maxc, maxr):
        x = ((maxc - minc) / 2) / 1920
        y = ((maxr - minr) / 2) / 1080
        width = (maxc - minc) / 1920
        high = (maxr - minr) / 1080
        return x, y, width, high

    with open(json_dir + json_file, 'r') as json_:
        json_ = json.load(json_)
        for shape in json_['shapes']:
            minc, minr = [float(temp) for temp in shape['points'][0]]
            maxc, maxr = [float(temp) for temp in shape['points'][1]]
            x, y, width, high = convert(minc, minr, maxc, maxr)
            txt_file.write("{} {} {} {}\n".format(x, y, width, high))
    print("finished convert json to txt! file name {}".format(json_file))
    txt_file.close()


