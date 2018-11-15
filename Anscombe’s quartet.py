import seaborn as sns

sns.set(style='ticks')

df= sns.load_dataset('anscombe')

sns.lmplot(x='x',y='y',col='dataset',hue='dataset',data=df,
           col_wrap=2,ci=None,palette='muted',
           scatter_kws={'s':50,'alpha':1})
sns.lmplot()