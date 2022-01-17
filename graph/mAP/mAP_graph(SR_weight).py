import numpy as np
import matplotlib.pyplot as plt
    
def one_graph(X=[], Y=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
    plt.figure()
    plt.title('mAP_graph(SR_128_weight)')
    
    coloring = ''
    if(typeof=='PSNR'):
        coloring = 'blue'
    else:
        coloring = 'red'
   
    plt.xlabel(Xlab)
    plt.ylabel(typeof)
    plt.grid()

    plt.plot(X,Y, label='previous '+typeof, color=coloring, linestyle='dashed', marker='o', 
             markersize =3, markerfacecolor=coloring)
     
    plt.savefig(savefolder+typeof+'.jpg')
    plt.close()

f = open("SR가중치사용.txt", 'r')

mAP=[]
epoch=[]
i=0

while True:
    line = f.readline()
    if not line: break
    new=(float)(line)
    mAP.append(new)
    i=i+1
    epoch.append(i)

print(mAP)   
newPath="./"
one_graph(epoch,mAP, "./",'mAP_graph(SR_weight)','Epoch')

f.close()