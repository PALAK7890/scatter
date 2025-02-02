import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")

print(df.groupby(['student_id','level'])['attempt'].mean())

mean=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()

fig=px.scatter(
    mean,x='student_id',
    y= 'level',
    size='attempt',
    color='attempt'
)
fig.show()