# author: roczhang
# file: txt_to_json.py
# time: 2021/05/10
import json
import re
import os
import glob
import cv2
# txt文件路径
txt_dir = "/data/file/yolo5/tmp/"
txts = os.listdir(txt_dir)
for file in txts:
    txt_name = os.path.splitext(file)

