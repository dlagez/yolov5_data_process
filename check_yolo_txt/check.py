import cv2 as cv
import os

txt_dir = '/data/file/yolo5/txt/'
img_dir = '/data/file/yolo5/粘连/334-666/'

txt_name = '334.txt'
img_name = '334.jpg'

with open(txt_dir + txt_name, 'r') as f:
    while True:
        file = f.readline()
        if not len(file):
            break
        print(file)