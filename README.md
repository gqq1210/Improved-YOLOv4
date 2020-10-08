# YOLOv4
YOLOv4 darknet

由于预训练模型权重文件过大，请自行下载yolov4.weights到主目录Improved-YOLOv4下，下载yolov4.conv.137到data目录下
data目录为重要目录
obj.data——各参数路径
obj.names——类别名称
backup——模型生成的权重文件
train.txt——训练集的文件路径
test.txt——测试集的文件路径
yolov4.cfg——模型参数以及网络结构
yolov4.conv.137——预训练模型权重文件

训练：./darknet.exe detector train data/obj.data data/yolov4.cfg data/backup/yolov4_1000.weights -gpus 0,1
测试：./darknet.exe detector test data/obj.data data/yolov4.cfg data/backup/yolov4.weights
