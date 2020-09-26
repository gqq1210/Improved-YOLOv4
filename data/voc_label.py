import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = []
# 这里是你的类别
classes = ["person", "bird", "cat", "cow", "dog", "horse", "sheep", "aeroplane", "bicycle", "boat", "bus", "car", "motorbike", "train",
           "bottle", "chair", "dining table", "potted plant", "sofa", "tv/monitor"]

#原样保留。size为图片大小
# 将ROI的坐标转换为yolo需要的坐标
# size是图片的w和h
# box里保存的是ROI的坐标（x，y的最大值和最小值）
# 返回值为ROI中心点相对于图片大小的比例坐标，和ROI的w、h相对于图片大小的比例
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(image_add):
    #image_add进来的是带地址的.jpg
    image_add = os.path.split(image_add)[1] #截取文件名带后缀
    image_add = image_add[0:image_add.find('.',1)] #删除后缀，现在只有文件名没有后缀
    print(image_add)
    #现在传进来的只有图片名没有后缀
   
    in_file = open('Annotations/' + image_add + '.xml')
    
    out_file = open('train/%s.txt'%(image_add), 'w')

    print(in_file)
    tree=ET.parse(in_file)
    root = tree.getroot()


    size = root.find('size')
    
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    #在一个XML中每个Object的迭代
    for obj in root.iter('object'):
        #iter()方法可以递归遍历元素/树的所有子元素
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        #如果训练标签中的品种不在程序预定品种，或者difficult = 1，跳过此object
        if cls not in classes or int(difficult)==1:
            continue
        #cls_id 只等于1
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        #b是每个Object中，一个bndbox上下左右像素的元组
        xmin = float(xmlbox.find('xmin').text)
        xmax = float(xmlbox.find('xmax').text)
        ymin = float(xmlbox.find('ymin').text)
        ymax = float(xmlbox.find('ymax').text)
        if(xmin > xmax):
            fff = xmin
            xmin = xmax
            xmax = fff
        if(ymin > ymax):
            fff = ymin
            ymin = ymax
            ymax = fff
        b = (xmin, xmax, ymin, ymax)
        bb = convert((w,h), b)
#         print(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        

if not os.path.exists('valid/'):
    os.makedirs('valid/')
image_adds = open("train.txt")
count = 0
for image_add in image_adds:
    #print(image_add)
    image_add = image_add.strip()
    #print (image_add)
    convert_annotation(image_add)
    count = count+1
print(count)
    
