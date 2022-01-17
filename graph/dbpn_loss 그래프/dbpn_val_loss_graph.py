import numpy as np
from matplotlib import pyplot as plt

def one_graph(X=[],Y=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
    plt.figure()
    plt.title('DBPN_Loss')
    
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
        
f = open("DBPN_avg_val_loss.txt", 'r')
dbpn_val_loss =[]
epoch=[]
i=0
while True:
    line = f.readline()
    line=line.split()
    if not line: break
    print(line[6])
    new=(float)(line[6])
    dbpn_val_loss.append(new)
    i=i+1
    epoch.append(i)

print(dbpn_val_loss)


one_graph(epoch,dbpn_val_loss, "./",'DBPN_Val_Loss','Epoch')

f.close()