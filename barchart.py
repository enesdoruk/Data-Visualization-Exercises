import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import math

menMeans=(20, 35, 30, 35, 27)
womenMeans=(25, 32, 34, 20, 25)
menStd=(2, 3, 4, 1, 2)
womenStd=(3, 5, 2, 3, 3)

ind= np.arange(len(menMeans))
width=0.35


fig,ax=plt.subplot()
rects1= ax.bar(ind=0.35/2,menMeans,width,yerr=menStd
               ,color='SkyBlue',label='men')
rects2=ax.bar(ind=0.35/2,womenMeans,width,yerr=womenStd
             ,color='blue',label='women')
ax.set_ylabel('scores')
ax.set_title('scores by group of gender')
ax.set_xticks(ind)
ax.set_xtickslabels('G1','G2','G3','G4','G5')
ax.legend()