def contrast_brightness_demo(img, img2,c,b):
    """利用图像的加权叠加来实现对比度的调整，以及亮度的调整，c代表对比度，b代表亮度"""
    # h, w, ch = img.shape #求出img的高和宽和通道数
    # blank = np.zeros([h,w,ch],dtype=np.uint8) #生成一张纯黑色图像
    dst = cv2.addWeighted(img,c,img2,1-c,b)
    #cv2.addWeighted()方法表示将img和blank两张图，按照c和1-c的比例加权叠加
    #由于blank是一张纯黑色的图，所有像素都是0，所以等价于将img的所有像素值乘上c(c>1也可以)
    #乘上c之后，2变4,4变8，不同像素之间的差异也就变大了，及对比度提高
    #b表示每个像素的每个通道的值加上b，也就是亮度提高
    # cv2.imshow("cb_dst",dst)
    # cv2.imwrite('/Users/apple/Desktop/'+str(c) + '_' + str(b) +'.jpg', dst)
    # cv2.waitKey()
    return dst



import os
import cv2
img = "/home/ubuntu/PycharmProjects/dection/darknet/data/images/"
dest = "/home/ubuntu/PycharmProjects/dection/darknet/data/blur/"
data = os.listdir(img)
count = 0
for img1 in data:
    i = img1.strip().split('.')
    if(i[-1] != 'txt'):
        kk = cv2.imread(img + img1)
        result = cv2.GaussianBlur(kk, (5,5),0)
        cv2.imwrite(dest + "blur_" + img1, result)
        count += 1
        print(count)

print(count)