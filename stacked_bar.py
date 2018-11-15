import pandas as pd 
import matplotlib.pyplot as plt
a =pd.DataFrame()
a['age']=[1,2,3,4,5,6,7]
a['height']=[50,70,90,110,120,130,145]
a['weight']=[5,10,15,18,20,22,24]
a['gender']=[1,1,0,1,0,0,0]




N=5
menMeans=(20, 35, 30, 35, 27)
womenMeans=(25, 32, 34, 20, 25)
menStd=(2, 3, 4, 1, 2)
womenStd=(3, 5, 2, 3, 3)
ind=np.arange(N)
width=0.35

p1=plt.bar(ind,menMeans,width,yerr=menStd)
p2=plt.bar(ind,womenMeans,width,bottom=menMeans,yerr=womenStd)

plt.ylabel('scores')
plt.title('scores by grouph of gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
