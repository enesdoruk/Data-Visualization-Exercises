import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
a =pd.DataFrame()
a['age']=[1,2,3,4,5,6,7]
a['height']=[50,70,90,110,120,130,145]
a['weight']=[5,10,15,18,20,22,24]
a['gender']=[1,1,0,1,0,0,0]

l = plt.plot(a['age'],a['gender'],'ro')
plt.setp(l,markersize=30)
plt.setp(l,markerfacecolor='C0')
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np


def f(t):
    'A damped exponential'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    return s1 * e1


t1 = np.arange(0.0, 5.0, .2)

l = plt.plot(t1, f(t1), 'ro')
plt.setp(l, markersize=30)
plt.setp(l, markerfacecolor='C0')

plt.show()

#%%






