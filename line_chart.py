import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


veriler = pd.read_csv('NBA_player_of_the_week.csv')

veriler.drop(veriler.columns[[1,2,3,5,6,7,8,10,12]], axis=1,inplace=True)



weight = veriler.iloc[:,3:]
y1=veriler['Seasons in league']
y1=pd.DataFrame(y1)



trace1 = go.Scatter(
        
        x=veriler.Age,
        y=veriler.Height,
        mode = "lines",
        marker = dict(color = 'rgba(80, 26, 80, 0.8)')
        
        )


trace2 = go.Scatter(
        
        x=veriler.Weight,
        y=veriler.Height,
        mode = "lines",
        marker = dict(color = 'rgba(200, 56, 80, 0.8)')
        
        )




data=[trace1,trace2]
fig = dict(data = data)
iplot(fig)


