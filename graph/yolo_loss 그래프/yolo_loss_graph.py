from matplotlib import pyplot as plt
import numpy as np
import graphing_yolo_box
import graphing_yolo_obj
import graphing_yolo_cls
import graphing_yolo_sum

f = open("DBPN_YOLO비교_0527.txt", 'r')
box_loss_list=[]
obj_loss_list=[]
cls_loss_list=[]
sum_loss_list=[]
epoch=[]
i=0 #epoch변경시 이것만 바꾸면됨 0으로 설정시 1부터 시작

while True:
    line = f.readline()
    line=line.split()
    if not line: break
    box_loss=(float)(line[6][8:-1])
    box_loss_list.append(box_loss)
    obj_loss=(float)(line[7][-11:-1])
    obj_loss_list.append(obj_loss)
    cls_loss=(float)(line[8][:-1])
    cls_loss_list.append(cls_loss)
    sum_loss=(float)(line[9][:-2])
    sum_loss_list.append(sum_loss)
    i=i+1
    epoch.append(i)

print(box_loss_list)
print(obj_loss_list)
print(cls_loss_list)
print(sum_loss_list)
newPath="./"
graphing_yolo_box.one_graph(epoch, box_loss_list, newPath,'yolo_box_loss','Epoch')
graphing_yolo_obj.one_graph(epoch, obj_loss_list, newPath,'yolo_obj_loss','Epoch')
graphing_yolo_cls.one_graph(epoch, cls_loss_list, newPath,'yolo_cls_loss','Epoch')
graphing_yolo_sum.one_graph(epoch, sum_loss_list, newPath,'yolo_sum_loss','Epoch')
 
f.close()