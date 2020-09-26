# import os
# img_path = 'test'
# data = os.listdir(img_path)
# f = open('test.txt','w')
# count = 0
# for value in data:
#     if(value[0] != '.' and value[-1] != 't'):
#         f.write('./data/test/'+value)
#         f.write('\n')
#         count = count + 1
#     else:
#         print("1")
# print(count)




import os
import shutil
img_path = "JPEGImages"
out_path = "train"
data = os.listdir(img_path)
# f = open('train.txt','r')
# alllines = f.readlines()
count = 0
for line in data:
    shutil.move("JPEGImages/" + line, "train/" + line)
    count = count + 1
print(count)


# 移动图片
# import os
# img_path = "test"
# data = os.listdir(img_path)
# count = 0
# for value in data:
#     count += 1
#
# print(count)


#修改JPG —>jpg 稍作改动
# import os
# img_path = "./data/images"
# data = os.listdir(img_path)
# count = 0
# for value in data:
#     a=value[-1]
#     # print(a[1])
#     if(a == 'G'):
#         os.rename(img_path + '/' + value[:-3] + 'JPG', img_path + '/' + value[:-3] + '.' + 'jpg')
#
#         count += 1
#
# print(count)


# 删除某张图片
# import os
# img_path = "./test_labels"
# data = os.listdir(img_path)
# count = 0
# for value in data:
#     a=value[0]
#     # print(a[1])
#     if(a == '.'):
#         os.remove(img_path + "/" + value)
#
#         count += 1
#
# print(count)




#
#
# import sys
# import os
# import json
# import xml.etree.ElementTree as ET
#
# START_BOUNDING_BOX_ID = 1
#
# # 注意下面的dict存储的是实际检测的类别，需要根据自己的实际数据进行修改
# # 这里以自己的数据集person和hat两个类别为例，如果是VOC数据集那就是20个类别
# # 注意类别名称和xml文件中的标注名称一致
# PRE_DEFINE_CATEGORIES = {"person":1, "hat":2}
#
#
# def get(root, name):
#     vars = root.findall(name)
#     return vars
#
#
# def get_and_check(root, name, length):
#     vars = root.findall(name)
#     if len(vars) == 0:
#         raise NotImplementedError('Can not find %s in %s.' % (name, root.tag))
#     if length > 0 and len(vars) != length:
#         raise NotImplementedError('The size of %s is supposed to be %d, but is %d.' % (name, length, len(vars)))
#     if length == 1:
#         vars = vars[0]
#     return vars
#
#
# def get_filename_as_int(filename):
#     try:
#         filename = os.path.splitext(filename)[0]
#         return int(filename)
#     except:
#         raise NotImplementedError('Filename %s is supposed to be an integer.' % (filename))
#
#
# def convert(xml_dir, json_file):
#     xmlFiles = os.listdir(xml_dir)
#
#     json_dict = {"images": [], "type": "instances", "annotations": [],
#                  "categories": []}
#     categories = PRE_DEFINE_CATEGORIES
#     bnd_id = START_BOUNDING_BOX_ID
#     num = 0
#     for line in xmlFiles:
#         #         print("Processing %s"%(line))
#         print(line)
#         num += 1
#         if num % 50 == 0:
#             print("processing ", num, "; file ", line)
#         # print("processing ",num,"; file ",line)
#         xml_f = os.path.join(xml_dir, line)
#         tree = ET.parse(xml_f)
#         root = tree.getroot()
#         ## The filename must be a number
#         filename = line[:-4]
#         image_id = get_filename_as_int(filename)
#         size = get_and_check(root, 'size', 1)
#         width = int(get_and_check(size, 'width', 1).text)
#         height = int(get_and_check(size, 'height', 1).text)
#         # image = {'file_name': filename, 'height': height, 'width': width,
#         #          'id':image_id}
#         image = {'file_name': (filename + '.jpg'), 'height': height, 'width': width,
#                  'id': image_id}
#         json_dict['images'].append(image)
#         ## Cruuently we do not support segmentation
#         #  segmented = get_and_check(root, 'segmented', 1).text
#         #  assert segmented == '0'
#         for obj in get(root, 'object'):
#             category = get_and_check(obj, 'name', 1).text
#             if category == 'person':
#                 print(category, ',', line)
#             if category == 'hat':
#                 print(category, ',', line)
#             if category not in categories:
#                 print(category, ',', line)
#                 new_id = len(categories)
#                 categories[category] = new_id
#             category_id = categories[category]
#             bndbox = get_and_check(obj, 'bndbox', 1)
#
#             xmin = float(get_and_check(bndbox, 'xmin', 1).text) - 1
#             ymin = float(get_and_check(bndbox, 'ymin', 1).text) - 1
#             xmax = float(get_and_check(bndbox, 'xmax', 1).text)
#             ymax = float(get_and_check(bndbox, 'ymax', 1).text)
#             if xmin > xmax:
#                 fff = xmin
#                 xmin = xmax
#                 xmax = fff
#             if ymin > ymax:
#                 fff = ymin
#                 ymin = ymax
#                 ymax = fff
#             # print(xmin,xmax,ymin,ymax)
#             assert (xmax > xmin)
#             assert (ymax > ymin)
#             o_width = abs(xmax - xmin)
#             o_height = abs(ymax - ymin)
#             ann = {'area': o_width * o_height, 'iscrowd': 0, 'image_id':
#                 image_id, 'bbox': [xmin, ymin, o_width, o_height],
#                    'category_id': category_id, 'id': bnd_id, 'ignore': 0,
#                    'segmentation': []}
#             json_dict['annotations'].append(ann)
#             bnd_id = bnd_id + 1
#
#     for cate, cid in categories.items():
#         cat = {'supercategory': 'none', 'id': cid, 'name': cate}
#         json_dict['categories'].append(cat)
#     json_fp = open(json_file, 'w')
#     json_str = json.dumps(json_dict)
#     json_fp.write(json_str)
#     json_fp.close()
#
#
# '''
# 在生成coco格式的annotations文件之前:
# 1.执行renameData.py对xml和jpg统一命名；
# 2.执行splitData方法，切分好对应的train/val/test数据集
# 3.执行splitImage方法，切分好对应的train/val/test数据集
# '''
# if __name__ == '__main__':
#     # folder_list = ["train", "val", "test"]
#     folder_list = "Annotations"
#     # 注意更改base_dir为本地实际图像和标注文件路径
#     base_dir = "./"
#     # for i in range(3):
#     folderName = folder_list
#     # xml_dir = base_dir + folderName + "/"
#     xml_dir = base_dir + folderName + "/"
#     json_dir = base_dir + "instances_" + folderName + ".json"
#
#     print("deal: ", folderName)
#     print("xml dir: ", xml_dir)
#     print("json file: ", json_dir)
#
#     convert(xml_dir, json_dir)