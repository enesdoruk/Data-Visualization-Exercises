import seaborn as sns

sns.set(style='ticks',palette='pastel')


tips= sns.load_dataset('tips')

sns.boxplot(x='day',y='total_bill',hue='smoker',palette=['m','g'],
            data=tips)


sns.despine(offset=10,trim=True)