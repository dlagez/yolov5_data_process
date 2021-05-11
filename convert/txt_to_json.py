# author: roczhang
# file: txt_to_json.py
# time: 2021/05/10
import json
import os

# txt文件路径
txt_dir = "/data/file/yolo5/tmp/"
txts = os.listdir(txt_dir)
for file in txts:
    file_name = os.path.splitext(file)[0]
    file = txt_dir + file

    with open(file, 'r', encoding="utf-8") as txt_file:
        shape = []
        for line in txt_file:
            line = [float(x) for x in line.strip().split()]
            label = str(int(line[0]))  # label
            points = []  # row clomn
            # yolo format
            x_center_pixel = line[1] * 1920
            y_center_pixel = line[2] * 1080
            width = line[3] * 1920
            high = line[4] * 1080
            # labelme format
            row_low = y_center_pixel - high / 2
            row_high = y_center_pixel + high / 2
            clomn_low = x_center_pixel - width / 2
            clomn_high = x_center_pixel + width / 2
            # row clomn json format
            points.append([clomn_low, row_low])
            points.append([clomn_high, row_high])
            # shape json
            shape.append({"label": label, "points": points, "group_id": None, "shape_type": "rectangle", "flags": {}})
            # print(shape)
        result = {"version": "4.5.6", "flags": {}, "shapes": shape, "imagePath": file_name + '.jpg', "imageData": None, "imageHeight": 1080, "imageWidth": 1920}
        print(result)
        json_path = "/data/file/yolo5/json/" + file_name + ".json"
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=4)

