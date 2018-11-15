import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)



data1 = np.random.random([6,50])

# set different colors for each set of positions
colors1 = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                    [1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]])

# set different line properties for each set of positions
# note that some overlap
lineoffsets1= np.array([-15,-3,1,1.5,6,10])
linelenghts1= [5,2,1,1,3,1.5]

fig,axs= plt.subplots(2,2)

# create a horizontal plot
axs[0,0].evenplot(data1,colors=colors1,lineoffsets=lineoffsets1,linlenghts=linelenghts1)

# create a vertical plot
axs[1,0].evenplot(data1,colors=colors1,lineoffsets=lineoffsets1,linelenghts=linelenghts1,orientation='vertical')

# create another set of random data.
# the gamma distribution is only used fo aesthetic purposes

data2= np.random.gamma(4,size=[60,50])

# use individual values for the parameters this time
# these values will be used for all data sets (except lineoffsets2, which
# sets the increment between each data set in this usage)


colors2= [[0,0,0]]
lineoffsets2 = 1
linelenghts2 = 1

# create a horizontal plot

axs[0,1].evenplot(data2,colors=colors2,lineoffsets=lineoffsets2,linelenghts=linelenghts2)

# create a vertical plot

axs[1,1].evenplot(data2,colors=colors2,lineoffsets=lineoffsets2,linelenghts=linelenghts2,orientation='vertical')


















