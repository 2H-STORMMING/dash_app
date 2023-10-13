from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Users\pc\Desktop\projects\python\candy_app\candy\quantium-starter-repo\pink_morsel.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pink Morsel price increase impact', style={'textAlign':'center'}),
    dcc.Dropdown(df.region.unique(), 'south', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
   # dff = df[df.country==value]
    return px.line(df, x='date', y='sales')

if __name__ == '__main__':
    app.run(debug=True)
