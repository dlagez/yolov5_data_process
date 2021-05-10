import json
import cv2
import os
"""
    img_names:所有图片的名字，得到路径下所有图片的名字
    img_paths:图片所在路径，得到某张图片的路径和名字
    labs_path：原始标签存放的位置。
"""
img_names = os.listdir('/media/ocean/大白菜U盘/mask-rcnn/label_test/20210510label/image_save')
img_paths = '/media/ocean/大白菜U盘/mask-rcnn/label_test/20210510label/image_save/'
labs_path = '/media/ocean/大白菜U盘/mask-rcnn/label_test/20210510label/image_label/'

for image_name in img_names:
    lab_name = image_name[:-3]
    lab_path = labs_path + lab_name + 'json'
    lab__new_path = img_paths + lab_name + 'json'
    f = open(lab_path, 'r')
    #file_name1 = '/media/ocean/大白菜U盘/mask-rcnn/label_test/1105-image.json'
    img = img_paths + image_name
    img = cv2.imread(img)
    h, w, c = img.shape
    content = f.read()
    a = json.loads(content)
    shape = []
    for i in range(len(a['rice'])):
        shape.append({"label": "rice", "points": a['rice'][i], "group_id": None, "shape_type": "polygon", "flags": {}})
    for j in range(len(a['broken_rice'])):
        shape.append({"label": "broken_rice", "points": a['broken_rice'][j], "group_id": None, "shape_type": "polygon", "flags": {}})
    result = {"version": "4.5.7", "flags": {}, "shapes": shape, "imagePath": image_name, "imageData": None, "imageHeight": h,
              "imageWidth": w, "lineColor": [0, 255, 0, 128], "fillColor": [255, 0, 0, 128]}
    f.close()

    with open(lab__new_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)