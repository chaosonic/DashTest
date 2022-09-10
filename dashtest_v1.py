from dash import Dash, dcc, html, Input, Output
from dash_bootstrap_components.themes import BOOTSTRAP

#import plotly
#import random
#import plotly.graph_objs as go
#import plotly.express as px

from src.components.layout import create_layout
from src.data.loader import load_transaction_data
#from collections import deque

#DATA_PATH = "./data/transactions.csv"

def main() -> None:

    # load the data and create the data manager
    data = load_transaction_data()

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app)




    app.run_server(debug=True)



if __name__ == "__main__":
    main()