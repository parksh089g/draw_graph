import numpy as np
import matplotlib.pyplot as plt
    
def one_graph(X=[], Y=[],X2=[],Y2=[],X3=[],Y3=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
    plt.figure()
    plt.title('mAP_graph')
    
    coloring = ''
    if(typeof=='PSNR'):
        coloring = 'blue'
    else:
        coloring = 'red'
   
    plt.xlabel(Xlab)
    plt.ylabel('mAP')
    plt.grid()

    plt.plot(X,Y)
    plt.plot(X2,Y2)
    plt.plot(X3,Y3) 
    plt.savefig(savefolder+typeof+'.jpg')
    plt.close()

f = open("result_HR.txt", 'r')
f2 = open("result_SR.txt", 'r')
f3 = open("result_SR2.txt", 'r')
mAP=[]
epoch=[]
i=0
mAP2=[]
epoch2=[]
i2=0
mAP3=[]
epoch3=[]
i3=0

while True:
    line = f.readline()
    if not line: break
    new=(float)(line)
    mAP.append(new)
    i=i+1
    epoch.append(i)

while True:
    line2 = f2.readline()
    if not line2: break
    new2=(float)(line2)
    mAP2.append(new2)
    i2=i2+1
    epoch2.append(i2)

while True:
    line3 = f3.readline()
    if not line3: break
    new3=(float)(line3)
    mAP3.append(new3)
    i3=i3+1
    epoch3.append(i3)

print(mAP)
print(mAP2)
print(mAP3)
print(epoch)
print(epoch2)
print(epoch3)     
newPath="./"
one_graph(epoch,mAP,epoch2,mAP2,epoch3,mAP3, "./",'mAP_graph','Epoch')

f.close()
f2.close()
f3.close()