# import os
# img_path = 'test_images/'
# data = os.listdir(img_path)
# f = open('test.txt','w')
# count = 0
# for value in data:
#     # a = value.strip().split('.')
#     # if(a[-1]!='txt'):
#     #     b = 'data/test_images/' + value
#     #     f.write(b)
#     #     f.write('\n')
#     #     count += 1
#     b = '/home/ubuntu/PycharmProjects/dection/darknet/data/test_images/' + value
#     f.write(b)
#     f.write('\n')
#     count += 1
# print(count)
#


#
# import os
# img_path = 'images/'
# data = os.listdir(img_path)
# f = open('train.txt','w')
# count = 0
# for value in data:
#     a = '/home/ubuntu/PycharmProjects/dection/darknet/data/images/'
#     value = a + value
#     i = value.strip().split('.')
#     if(i[-1] == 'jpg'):
#         f.write(value)
#         f.write('\n')
#         count += 1
# print(count)







#
# import cv2
# f = open('train.txt','r')
# alllines=f.readlines()
# f.close()
# f=open('train-fog.txt','w+')
# for line in alllines:
#     a=line.strip().split('/')
#     a=a[0] + '/' + a[1] + '/' + 'fog_' + a[-1]
#     print(a)
#     f.write(a)
#     f.write('\r\n')
#


#
# import cv2
# a = "images"
# # print('\'' + a[0] + '\'')
# image = cv2.imread(a)
# print(image)
# f.close()
#
#
#
#

# import cv2
# f = open('name.txt','r')
# alllines=f.readlines()
# f.close()
# f=open('name.txt','w+')
# for line in alllines:
#     a=line.strip().split('.')
#     b=a[0]
#     f.write(b)
#     f.write('\r\n')







#
#
# import os, random, shutil
# def moveFile(fileDir):
#         pathDir = os.listdir(fileDir)    #取图片的原始路径
#         filenumber=len(pathDir)
#         rate=0.2    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
#         picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
#         sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
#         labelfile = "txt/"
#         labeltar = "test/"
#         print (sample)
#         for name in sample:
#             a=name.strip().split('.')
#             a=a[0]+'.txt'
#             shutil.move(fileDir+name, tarDir+name)
#             shutil.move(labelfile+a, labeltar+a)
#
#         return
#
# if __name__ == '__main__':
#     fileDir = "JPEGImages/"    #源图片文件夹路径
#     tarDir = 'test/'    #移动到新的文件夹路径
#     moveFile(fileDir)
#


# import os
# path = "images/"
# data = os.listdir(path)
# c = 0
# for i in data:
#     va = i.strip().split('.')
#     if(va[-1]!='jpg'):
#         print(i)
#         print(path+va[0]+'.jpg')
#         os.rename(path+i, path+va[0]+'.jpg')
#     c += 1
# print(c)


# import os
# path = "images/"
# lab = "annotations/"
# imgdata = os.listdir(path)
# labdata = os.listdir(lab)
# count = 0
# for i in labdata:
#     name = i.strip().split('.')
#     # print(name[0])
#     if(len(name[0]) <= 8):
#         count += 1
#         # os.remove(path + i)
#         os.remove(lab + name[0] + '.xml')
# print(count)




# import os
# import shutil
# file = '/home/ubuntu/PycharmProjects/dection/darknet/data/images/'
# data = os.listdir(file)
# count = 0
# for i in data:
#     value = i.strip().split('.')
#     if(value[-1] == 'txt'):
#         # shutil.copy(file + i, file + 'rain_' + i)
#         # shutil.copy(file + i, file + 'fog_' + i)
#         # shutil.copy(file + i, file + 'blur_' + i)
#
#         count += 1
# print(count)



import os
import shutil
# old = 'valid/'
# new = 'test_images/'
# count = 0
# data = os.listdir(new)
# for i in data:
#     # shutil.move(old + i, new + i)
#     count += 1
# print(count)