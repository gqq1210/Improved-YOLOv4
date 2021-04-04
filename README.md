# YOLOv4
YOLOv4 darknet

由于预训练模型权重文件过大，请自行下载yolov4.weights到主目录Improved-YOLOv4下，下载yolov4.conv.137到data目录下  
yolov4.weights链接: https://pan.baidu.com/s/1gHljFNacH4n9xmWFOART6Q  密码: 30dk  
yolov4.conv.137链接: https://pan.baidu.com/s/1HfwVztoAJMUhw_XQj09k2w  密码: tpnl  

### 环境  
Ubuntu 16.04  
Python3.6  
cuda 10  

### Model
![](https://github.com/gqq1210/Improved-YOLOv4/blob/91ee3441a30fefddbaa089993c35d49320e79ed9/screenshots/model.png)
  
用gpu加速，打开makefile文件修改参数，修改完后直接make  
GPU=1  
OPENCV=1  
在data路径下分别新建train和test文件夹，用于存放训练集和测试集，并将这些图片的路径分别记录在train.txt和test.txt中  

### data目录为重要目录

文件            | 用途
------         | ------
obj.data       | 各参数路径  
obj.names      | 类别名称  
backup         | 模型生成的权重文件  
train.txt      | 训练集的文件路径  
test.txt       | 测试集的文件路径  
yolov4.cfg     | 模型参数以及网络结构  
yolov4.conv.137| 预训练模型权重文件  


### train/test
train: ``./darknet.exe detector train data/obj.data data/yolov4.cfg data/backup/yolov4_1000.weights -gpus 0,1``  
  
test: ``./darknet.exe detector test data/obj.data data/yolov4.cfg data/backup/yolov4.weights``
