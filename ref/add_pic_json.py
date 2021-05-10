# 此函数用于找到json文件对应的图片并放入一个文件夹完成预标注
import json
import os
import glob
from PIL import Image
# json文件路径
json_dir_name = "D:/python/yolov5-master/inference/json_save"
json_pattern = os.path.join(json_dir_name, '*.json')
file_list = glob.glob(json_pattern)
for file in file_list:
    # 找到图片路径
    name1 = os.path.basename(file)
    name = os.path.splitext(name1)[0]
    pic_name = name + '.jpg'
    pic_path = "D:/python/yolov5-master/inference/images/" + pic_name
    # 设置图片存储路径
    pic_savepath = "D:/python/yolov5-master/inference/add_pj/" + pic_name
    # 存储图片
    I = Image.open(pic_path)
    I.save(pic_savepath)
    # 存储json文件
    json_savepath = "D:/python/yolov5-master/inference/add_pj/" + name1
    with open(file) as json_file:
        data = json.load(json_file)
    # 将字典转换为字符串
    json_str = json.dumps(data, indent=4)
    # 将字典写入json文件中
    with open(json_savepath, 'w') as json_file:
        json_file.write(json_str)