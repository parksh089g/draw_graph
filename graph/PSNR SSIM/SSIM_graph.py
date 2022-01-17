import numpy as np
from matplotlib import pyplot as plt

def one_graph( X =[], Y=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
    plt.figure()
    plt.title('SSIM')
    
    coloring = ''
    if(typeof=='SSIM'):
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
        
f = open("base2SSIM.txt", 'r')
SSIM =[]
epoch=[]
i=0
while True:
    line = f.readline()
    line=line.split()
    if not line: break
    new=(float)(line[4])
    SSIM.append(new)
    i=i+1
    epoch.append(i)

print(SSIM)


one_graph(epoch,SSIM, "./",'SSIM','Epoch')

f.close()