import matplotlib.pyplot  as plt
import numpy as np



data ={'apples':10,'oranges':15,'lemons':5,'watermelon':50}
names=list(data.keys())
values=list(data.values())


fig,axs= plt.subplots(1,3,figsize=(20,20),sharey=True)

axs[0].bar(names,values)
axs[1].scatter(names,values)
axs[2].plot(names,values)

fig.suptitle('categorical plotting')
plt.show()