# author: roczhang
# file: json_to_txt.py
# time: 2021/05/11
import json
import os

# 将json文件夹转换成txt（yolo格式）
json_dir = '/data/file/yolo5/粘连/334-666/'
json_files = os.listdir(json_dir)

txt_dir = '/data/file/yolo5/txt/'
if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

for json_file in json_files:
    if json_file.split('.')[1] == 'jpg':
        continue
    # json_file = '1.json'
    txt_name = json_file.split('.')[0] + '.txt'
    # print(txt_name)
    txt_file = open(os.path.join(txt_dir, txt_name), 'w')

    def convert(x1, y1, x2, y2):
        x = ((x1 + x2) / 2) / 1920
        y = ((y1 + y2) / 2) / 1080
        width = abs((x1 - x2) / 1920)
        high = abs((y1 - y2) / 1080)
        return x, y, width, high

    with open(json_dir + json_file, 'r', encoding='utf-8') as json_:
        json_ = json.load(json_)
        for shape in json_['shapes']:
            x1, y1 = shape['points'][0]
            x2, y2 = shape['points'][1]

            # minc, minr = [float(temp) for temp in shape['points'][0]]
            # maxc, maxr = [float(temp) for temp in shape['points'][1]]
            x, y, width, high = convert(x1, y1, x2, y2)
            txt_file.write("0 {} {} {} {}\n".format(x, y, width, high))
    print("finished convert json to txt! file name {}".format(json_file))
    txt_file.close()