import json
import re
import os
import glob
import cv2
# txt文件路径
txt_dir_name = "D:/python/yolov5-master/inference/111"
json_pattern = os.path.join(txt_dir_name, '*.txt')
file_list = glob.glob(json_pattern)
for file in file_list:
    # 找到图片名
    name1 = os.path.basename(file)
    name = os.path.splitext(name1)[0]
    pic_name = name + '.jpg'
    pic_path = "D:/python/yolov5-master/inference/images/" + pic_name
    img = cv2.imread(pic_path)
    h, w, c = img.shape
    # 读取文件
    with open(file, 'r', encoding="utf-8") as txt_file:
        # 建立shape用以存储shapes里面的数据
        shape = []
        # 逐行读取
        for line in txt_file:
            # 每一行是一个字典
            # 将第一行数据按空格切分
            line = line.strip().split()
            label_n = line[0]
            points1 = []
            points1.append([float(line[1]), float(line[2])])
            points1.append([float(line[3]), float(line[4])])
            shape.append({"label": label_n, "points": points1, "group_id": None, "shape_type": "rectangle", "flags": {}})
    # 创建一个字典
    result = {"version": "4.5.6", "flags": {}, "shapes": shape, "imagePath": pic_name, "imageData": None, "imageHeight": h, "imageWidth": w, "lineColor": [0, 255, 0, 128], "fillColor": [255, 0, 0, 128]}
    # 设置json存储路径
    json_path = "D:/python/yolov5-master/inference/json_save/" + name + ".json"
    # 将字典转换为字符串
    # json_str = json.dumps(result, indent=4)
    # 将字典写入json文件中
    with open(json_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)
        #json_file.write(json_str)