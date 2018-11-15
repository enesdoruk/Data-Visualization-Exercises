import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0,10,0.01)

ax1= plt.subplot(211)
ax1.plot(t,np.sin(2*np.pi*t))

ax2= plt.subplot(212, sharex=ax1)
ax2.plot(t,np.sin(4*np.pi*t))

plt.show()
