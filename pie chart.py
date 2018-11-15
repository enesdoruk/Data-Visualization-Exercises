import matplotlib.pyplot as plt


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'frogs','hogs','logs','dogs'

sizes = [15,30,45,10]

explode= (0,0.1,0,0)# only "explode" the 2nd slice (i.e. 'Hogs')

fig,ax = plt.subplots()

ax.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%',shadow=True,startangle=90)

ax.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()