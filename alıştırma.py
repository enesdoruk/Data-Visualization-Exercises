#%%
import pandas as pd 
import matplotlib.pyplot as plt
a =pd.DataFrame()
a['age']=[1,2,3,4,5,6,7]
a['height']=[50,70,90,110,120,130,145]
a['weight']=[5,10,15,18,20,22,24]
a['gender']=[1,1,0,1,0,0,0]
#%%
x = a['age']
y=a['height']
plt.plot(x,y)
plt.show()
plt.scatter(x,y,marker='+',alpha=0.5,edgecolors='r')
plt.show()

plt.hist(x)
#%%
import seaborn as sns 
#%%
f,ax=plt.subplots(figsize=(18,18))

sns.heatmap(a.corr(),annot=True,linewidths=5,linecolor='red',ax=ax,
            fmt='.1f')

#%%
a.plot(x='age',y='height',kind='scatter')
plt.scatter(a.age,a.height)
#%%

def top(a,b):
    
    a =input('a gir:')
    b= input('b gir')
    return a+b








#%%
a=2
b=3

def kok():
   
    d= pow(a,1/2)
    return d
    
    def top():
        
        c= a+b
        return c
    
        def kare():
            
            a=pow(a)
            b=pow(b)
            return a,b











#%%

number_list =[1,2,3,4,5,6,7,8]
y=map(lambda x:pow(x,2),number_list)
print(list(y))



list1 =[1,2,3,4]
list2=[5,6,7,8]
z=zip(list1,list2)
print(list(z))
#%%
import pandas as pd
list3 =[]
for x in range(0,50,2):
    list3.append(x)

num1=[1,2,34,4]
num2=[i+1 for i in num1]
q=pd.DataFrame(num1)
#%%


print(a['age'].value_counts(dropna=False))



a.boxplot(column='age',by='height')


data_new=a.head()
melted=pd.melt(frame=data_new,id_vars='Index',value_vars=['age','gender'])

#%%



