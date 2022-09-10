#import pandas as pd
#import random
import plotly.express as px
#import plotly
#import plotly.graph_objs as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from collections import deque
import random

#from . import ids

def renderGraph(app: Dash) -> html.Div:

    # X = deque(maxlen=20)
    # X.append(1)
    # Y = deque(maxlen=20)
    # Y.append(1)



    stocks = ['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT']

    @app.callback(Output('live-graph', 'figure'),
                Input('graph-update', 'n_intervals')
                )
    def update_graph_scatter(timer) -> html.Div:
    
        STOCK_DATA = px.data.stocks()
        # X.append(X[-1]+1)
        # Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
        # fig = px.line(
        #         x=list(X),
        #         y=list(Y),
        #         range_x= [min(X),max(X)],
        #         range_y= [min(Y),max(Y)]
        #         )
        fig = px.line(x=STOCK_DATA['date'],
        y = STOCK_DATA[stocks[random.randint(0,5)]]
        )

        #return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
        #                                            yaxis=dict(range=[min(Y),max(Y)]),)}
        return fig 
    
    return html.Div(
        [
            dcc.Graph(id='live-graph', figure={}),
            dcc.Interval(
                id='graph-update', n_intervals=0, interval=5*1000
            ),
        ]
    )
