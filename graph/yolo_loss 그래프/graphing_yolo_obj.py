import os
import numpy as np
import matplotlib.pyplot as plt

def one_graph(X=[], Y=[], savefolder ='./', typeof='L1 loss', Xlab='epoch'):
    plt.figure()
    
    plt.title('Yolo obj loss graph')
    
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
