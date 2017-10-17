import plotly.offline as py
import plotly.graph_objs as go
from numpy import arange, array, ones, genfromtxt
from scipy import stats
import pandas as pd
import numpy as np

def makePlot(data,data2,name):
    tracee = []
    trace = go.Scatter(
        x=data, y=data2
    )
    tracee.append(trace)

    data = tracee

    fig = dict(data=data)

    py.plot(fig, filename=name, validate=False)