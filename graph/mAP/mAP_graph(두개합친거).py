import numpy as np
import matplotlib.pyplot as plt
    
def one_graph(X=[], Y=[],X2=[],Y2=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
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
    plt.savefig(savefolder+typeof+'.jpg')
    plt.close()

f = open("SR가중치사용.txt", 'r')
f2 = open("HR가중치사용.txt", 'r')
mAP=[]
epoch=[]
i=0
mAP2=[]
epoch2=[]
i2=0

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

print(mAP)
print(mAP2)
print(epoch)
print(epoch2)   
newPath="./"
one_graph(epoch,mAP,epoch2,mAP2, "./",'mAP_graph','Epoch')

f.close()
f2.close()