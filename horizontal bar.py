import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
f,ax=plt.subplots()


people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos=np.arange(len(people))
performance=3+10*np.random.rand(len(people))
error=np.random.rand(len(people))

ax.barh(y_pos,performance,xerr=error,align='center',color='green',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('performance')
ax.set_title('enes')
plt.show()