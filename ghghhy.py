import csv 
import plotly.express as px
import numpy as np

with open ("Hehe Stupidity Go Brr") as stupidName
df = csv.DictReader(stupidName)
fig = px.line(df, x="Days Present", y="Marks In Percentage")
fig.show 

x = np.arrange(180, 160, 155, 145, 122)
y = np.array([79, 73, 60, 59.59, 30])