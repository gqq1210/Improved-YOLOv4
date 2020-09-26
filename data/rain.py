#rain
import cv2
import numpy as np
import os


def get_noise(img, value=10):
    noise = np.random.uniform(0, 256, img.shape[0:2])
    # 控制噪声水平，取浮点数，只保留最大的一部分作为噪声
    v = value * 0.01
    noise[np.where(noise < (256 - v))] = 0

    # 噪声做初次模糊
    k = np.array([[0, 0.1, 0],
                  [0.1, 8, 0.1],
                  [0, 0.1, 0]])

    noise = cv2.filter2D(noise, -1, k)

    # 可以输出噪声看看
    # cv2.imshow('img',noise)
    # cv2.waitKey()
    # cv2.destroyWindow('img')
    return noise


def rain_blur(noise, length=10, angle=0, w=1):

    # 将噪声加上运动模糊,模仿雨滴
    #
    # >>>输入
    # noise：输入噪声图，shape = img.shape[0:2]
    # length: 对角矩阵大小，表示雨滴的长度
    # angle： 倾斜的角度，逆时针为正
    # w:      雨滴大小
    #
    # >>>输出带模糊的噪声

    # 这里由于对角阵自带45度的倾斜，逆时针为正，所以加了-45度的误差，保证开始为正
    trans = cv2.getRotationMatrix2D((length / 2, length / 2), angle - 45, 1 - length / 100.0)
    dig = np.diag(np.ones(length))  # 生成对焦矩阵
    k = cv2.warpAffine(dig, trans, (length, length))  # 生成模糊核
    k = cv2.GaussianBlur(k, (w, w), 0)  # 高斯模糊这个旋转后的对角核，使得雨有宽度

    # k = k / length                         #是否归一化

    blurred = cv2.filter2D(noise, -1, k)  # 用刚刚得到的旋转后的核，进行滤波

    # 转换到0-255区间
    cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
    blurred = np.array(blurred, dtype=np.uint8)

    # cv2.imshow('img',blurred)
    # cv2.waitKey()
    # cv2.destroyWindow('img')

    return blurred


def alpha_rain(rain, img, beta=0.8):
    # 输入雨滴噪声和图像
    # beta = 0.8   #results weight
    # 显示下雨效果

    # expand dimensin
    # 将二维雨噪声扩张为三维单通道
    # 并与图像合成在一起形成带有alpha通道的4通道图像
    rain = np.expand_dims(rain, 2)
    rain_effect = np.concatenate((img, rain), axis=2)  # add alpha channel

    rain_result = img.copy()  # 拷贝一个掩膜
    rain = np.array(rain, dtype=np.float32)  # 数据类型变为浮点数，后面要叠加，防止数组越界要用32位
    rain_result[:, :, 0] = rain_result[:, :, 0] * (255 - rain[:, :, 0]) / 255.0 + beta * rain[:, :, 0]
    rain_result[:, :, 1] = rain_result[:, :, 1] * (255 - rain[:, :, 0]) / 255 + beta * rain[:, :, 0]
    rain_result[:, :, 2] = rain_result[:, :, 2] * (255 - rain[:, :, 0]) / 255 + beta * rain[:, :, 0]
    # 对每个通道先保留雨滴噪声图对应的黑色（透明）部分，再叠加白色的雨滴噪声部分（有比例因子）

    # cv2.imshow('rain_effct_result', rain_result)
    # cv2.imwrite('/Users/apple/Desktop/mm.jpg', rain_result)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return rain_result





img = "/home/ubuntu/PycharmProjects/dection/darknet/data/images/"
dest = "/home/ubuntu/PycharmProjects/dection/darknet/data/rain/"
data = os.listdir(img)
count = 0
for i in data:
    k = i.strip().split('.')
    if (k[-1] != 'txt'):
        image = cv2.imread(img + i)
        noise = get_noise(image, value = 20)
        rain = rain_blur(noise, length = 25, angle = 25, w = 3)
        result = alpha_rain(rain, image)
        cv2.imwrite(dest + "rain_" +i, result)
        count += 1
        print(count)


print(count)










# fog-------------高斯模糊
# import os
# import cv2
# img = "/Users/apple/Desktop/fog/train/"
# dest = "/Users/apple/Desktop/fog/mohu/"
# data = os.listdir(img)
# count = 0
# for i in data:
#     image = cv2.imread(img + i)
#     result = cv2.GaussianBlur(image, ksize=(21, 21), sigmaX=0, sigmaY=0)
#     cv2.imwrite(dest + i, result)
#     count += 1
#     print(count)
#     os.remove(img + i)
#
# print(count)

# import cv2
# import numpy as np
# img1 = "/Users/apple/Desktop/kk.jpg"
# img2 = "/Users/apple/Desktop/rain.jpg"
# image = cv2.imread(img1)
# noise = get_noise(image, value = 20)
# rain = rain_blur(noise, length = 25, angle = 25, w = 3)
# result = alpha_rain(rain, image)
# cv2.imwrite(img2, result)
# 
# 






#
# def contrast_brightness_demo(img, img2,c,b):
#     """利用图像的加权叠加来实现对比度的调整，以及亮度的调整，c代表对比度，b代表亮度"""
#     # h, w, ch = img.shape #求出img的高和宽和通道数
#     # blank = np.zeros([h,w,ch],dtype=np.uint8) #生成一张纯黑色图像
#     dst = cv2.addWeighted(img,c,img2,1-c,b)
#     #cv2.addWeighted()方法表示将img和blank两张图，按照c和1-c的比例加权叠加
#     #由于blank是一张纯黑色的图，所有像素都是0，所以等价于将img的所有像素值乘上c(c>1也可以)
#     #乘上c之后，2变4,4变8，不同像素之间的差异也就变大了，及对比度提高
#     #b表示每个像素的每个通道的值加上b，也就是亮度提高
#     # cv2.imshow("cb_dst",dst)
#     cv2.imwrite('/Users/apple/Desktop/'+str(c) + '_' + str(b) +'.jpg', dst)
#     # cv2.waitKey()
#     # return dst



#
# import cv2
# import numpy as np
# img1 = "/Users/apple/Desktop/kk.jpg"
# img2 = "/Users/apple/Desktop/1.jpg"
# img1 = cv2.imread(img1)
# img2 = cv2.imread(img2)
# h = img1.shape[0]
# w = img1.shape[1]
# img2 = img2[0:h, 0:w]
# contrast_brightness_demo(img1, img2,0.6,0)







# import os
# import cv2
# img = "/Users/apple/Desktop/fog/train/"
# dest = "/Users/apple/Desktop/fog/fog/"
# data = os.listdir(img)
# img2 = "/Users/apple/Desktop/fog/1.jpg"
# count = 0
# for img1 in data:
#     kk = cv2.imread(img + img1)
#     gg = cv2.imread(img2)
#     h = kk.shape[0]
#     w = kk.shape[1]
#     gg = gg[0:h, 0:w]
#     result = contrast_brightness_demo(kk, gg, 0.5, 0)
#     cv2.imwrite(dest + img1, result)
#     count += 1
#     print(count)
#     os.remove(img + img1)
#
# print(count)
