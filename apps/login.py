#import flask
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

layout = html.Div(id='login', children=[
             html.H2('Login Form'),
             html.Div(id="hidden_div_for_redirect_callback"),
             html.Form([
               html.P(children=["Username : ", dcc.Input(type="text", name="username", id="username", placeholder="Enter username")]),
               html.P(children=["Password : ", dcc.Input(type="password", name="password", id="password", placeholder="Enter password")]),  
               html.Button(children=["submit"], type="submit", id="login-btn"),
             ], method="post"),
         ])        

@app.callback(Output("hidden_div_for_redirect_callback","children"),
              [Input("login-btn", "n_clicks")],
              [State("username", 'value'), State("password",'value'),])
def login_user(n_clicks, uname, passwd):
    print("n_click : ",n_clicks)
    print("uname : ",uname)
    print("passwd : ",passwd)
    if (uname is not None) and (passwd is not None) and (n_clicks is not None):
      print("we are here")
      return dcc.Location(pathname="/apps/app1", id="hidden-non")
    elif (n_clicks is not None):
      return html.Markdown("Invalid username or password")
    else:
        pass  
