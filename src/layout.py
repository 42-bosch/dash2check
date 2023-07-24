from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
from data import get_data_dtc

def layout():
    
    return dbc.Container(
        [
            dbc.Row(
                [
                    html.H1("Dashboard"),
                    html.Span("Example: 0240265"),
                    html.P(),
                ],
            ),
            dbc.Row(
                [
                    html.Div(
                        [
                            html.Div(dcc.Input(id="input-on-submit", type="text")),
                            html.Button("Submit", id="submit-val", n_clicks=0),
                            html.Div([dcc.Graph(id="line-graph", figure=px.line(get_data_dtc(), template="plotly_dark"))]),
                            dcc.Loading(id="output-graph", type="circle", children=[]),
                        ]
                    ),
                ],
            ),
        ],
    )
    
def callbacks():
    @callback(
        Output("output-graph", "children"),
        Input("submit-val", "n_clicks"),
        State("input-on-submit", "value"),
    )
    def update_output(children, value):
        if value is None:
            return html.Div()

        if value.isnumeric() is False:
            return html.Div("Value is not a valid FIPE code")

        data = get_data_dtc()

        fig = px.line(data, x="mes", y="valor", color="ano", template="plotly_dark")

        return html.Div([dcc.Graph(id="line-graph", figure=fig)])