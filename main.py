import dash
from app import main_layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = main_layout

if __name__ == '__main__':
    app.run_server(debug=True,port=8051)
