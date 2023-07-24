from dash import Dash
import dash_bootstrap_components as dbc
import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = layout.layout()

layout.callbacks()

if __name__ == "__main__":
    app.run_server(debug=False)
