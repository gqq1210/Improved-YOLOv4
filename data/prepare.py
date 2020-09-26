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
img = "/Users/apple/Desktop/fog/train/"
dest = "/Users/apple/Desktop/fog/fog/"
data = os.listdir(img)
img2 = "/Users/apple/Desktop/fog/1.jpg"
count = 0
for img1 in data:
    kk = cv2.imread(img + img1)
    gg = cv2.imread(img2)
    h = kk.shape[0]
    w = kk.shape[1]
    gg = gg[0:h, 0:w]
    result = contrast_brightness_demo(kk, gg, 0.5, 0)
    cv2.imwrite(dest + img1, result)
    count += 1
    print(count)
    os.remove(img + img1)

print(count)