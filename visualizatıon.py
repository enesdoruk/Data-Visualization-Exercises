#%%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}

group_data = list(data.values())
group_names = list(data.keys())
group_mean =np.mean(group_data)

fig,ax = plt.subplots(figsize=(10,6))
ax.barh(group_names,group_data)
plt.style.use('fivethirtyeight')
labels =ax.get_xticklabels()

plt.setp(labels,rotation=45,horizontalalignment='right')
ax.set(xlim=[-10000, 140000],xlabel='total revanue',ylabel='company'
       ,title='company revanue')
def currency(x, pos):
   
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

formatter = FuncFormatter(currency)

ax.xaxis.set_major_formatter(formatter)


ax.axvline(group_mean,ls='--',color='r')


for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")
ax.title.set(y=1.05)

ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])




plt.show()
#%%


import numpy as np


maas =[100,13,44,23,56,13,68]

x = np.max(maas)-np.min(maas)
var = sum((maas-np.mean(maas))**2)/len(maas)
std = np.sqrt(var)










