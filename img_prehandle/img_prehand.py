# author: roczhang
# file: img_prehand.py
# time: 2021/04/24
import numpy as np
import imgaug.augmenters as iaa
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio
import os
old_path = '/data/file/image13_2label/train_img/'
new_path = '/data/file/image13_2label/train_img_mask/'


def img_pro(old_path, new_path):
    img_list = os.listdir(old_path)
    num = 1
    for img in img_list:
        old_img = old_path + img
        img_save = new_path + img
        old_img = imageio.imread(old_img)
        aug = iaa.Cutout(nb_iterations=250, size=[0.03, 0.04], cval=0)
        img_mask = aug.augment_image(old_img)
        print("img number:", num, 'processing img_name:', img)
        num += 1
        imageio.imwrite(img_save, img_mask)
img_pro(old_path, new_path)