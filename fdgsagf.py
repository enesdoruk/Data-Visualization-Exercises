import matplotlib.pyplot as plt
import numpy as np
#%%
fig = plt.figure()
fig,ax = plt.subplots(2,2)
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

data = pd.read_csv('complete.csv')

data.columns = map(str.lower,data.columns)
x = data.iloc[:,30:]
y=['id','full_name','club_logo','birth_date','body_type','real_face','flag',
   'photo','eur_wage','eur_release_clause']
data.drop(x,inplace=True,axis=1)
data.drop(y,inplace=True,axis=1)
data.fillna(0)
missing = data.isnull().sum()
#print(missing)
totalmissing = missing.sum()
print(totalmissing)

#from sklearn.preprocessing import Imputer
#
#imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
#imputer = imputer.fit(data[:,7:])
#data[:,7:] =imputer.transform(data[:,7:])

fig, ax = plt.subplots()
ax.set_xticks(np.arange(len(data.age)))
ax.set_yticks(np.arange(len(data.phy)))

ax.set_xticklabels(data.age)
ax.set_yticklabels(data.phy)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

fig.tight_layout()
plt.show()


#%%