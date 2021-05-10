# author: roczhang
# file: rice_labels.py
# time: 2021/04/22
from skimage import io
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import matplotlib.patches as mpatches
from skimage import data, filters, segmentation, measure, morphology, color


file_path = '/data/file/rice_frame/images/'
file_names = os.listdir(file_path)
# file_name = file_names[0]

for file_name in file_names:
    file_name_only = file_name.split('.')[0]
    file_name = file_path+file_name
    # img_name = str(file_num)+'.jpg'

    rice_img = io.imread(file_name)

    # convert image to gray
    rice_img = rgb2gray(rice_img)
    height, width = rice_img.shape
    thresh = filters.threshold_otsu(rice_img)  # 阈值分割
    bw = morphology.closing(rice_img > thresh)  # 闭运算

    cleared = bw.copy()
    # cleared = segmentation.clear_border(cleared)  # 清除与边界相连的目标物

    label_image = measure.label(cleared)  # 连通区域的标记
    borders = np.logical_xor(bw, cleared)  # 异或
    label_image[borders] = -1

    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))
    # ax1.imshow(cleared, plt.cm.gray)
    # ax2.imshow(label_image)

    file_label = open('/data/file/rice_frame/labels/'+file_name_only+'.txt', 'a')
    for region in measure.regionprops(label_image):
        if region.area < 100:
            continue
        minr, minc, maxr, maxc = region.bbox
        num = 1
        minr, minc = minr-num, minc-num
        maxr, maxc = maxr+num, maxc+num
        x_center = ((maxc + minc)/2)/width
        y_center = ((maxr + minr)/2)/height
        width_label = (maxc - minc)/width
        height_label = (maxr - minr)/height
        label = '0 ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width_label) + ' ' + str(height_label)+'\n'
        file_label.write(label)
        print(label)
        # rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=0.5)
print('标签已经完成！')
