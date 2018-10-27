import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import plotly.plotly as py
import plotly.graph_objs as go

from flask import send_file
import base64
import datetime
import io

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import SpectralClustering

app = dash.Dash("Wells-Carbo", external_stylesheets=external_stylesheets)
server = app.server
app.config['suppress_callback_exceptions']=True

app.layout = html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
