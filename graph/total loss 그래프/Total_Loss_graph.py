import numpy as np
from matplotlib import pyplot as plt

def one_graph(X=[], Y=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
    plt.figure()
    
    plt.title('Total Loss Graph')
    
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


f = open("DBPN+YOLO합친 로스.txt", 'r')

Total_Loss =[]
epoch=[]
i=0

while True:
    line = f.readline()
    line=line.split()
    if not line: break
    Total_Loss.append(float(line[0]))
    i=i+1
    epoch.append(i)

one_graph(epoch, Total_Loss, "./",'Total_Loss','Epoch')
