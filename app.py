from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Users\pc\Desktop\projects\python\candy_app\candy\quantium-starter-repo\pink_morsel.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pink Morsel price increase impact', style={'textAlign':'center'}),
    dcc.Dropdown(df.region.unique(), 'south', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    dcc.Dropdown(df.region.unique(), 'south', id='dropdown-selection1'),
    dcc.Graph(id='graph1-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.region==value]
    return px.line(dff, x='date', y='sales')


@callback(
    Output('graph1-content', 'figure'),
    Input('dropdown-selection1', 'value')
)


def update_graph1(value):
    dff = df[df.region==value]
    return px.line(dff, x='date', y='quantity')

if __name__ == '__main__':
    app.run(debug=True)
