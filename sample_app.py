# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    "background":'#111111',
    "text":"#7FBDFF"
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns ])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in (range(min(len(dataframe), max_rows))) 
        ])
    ])

df = pd.DataFrame({
    "Fruit":["Apple","Orange","Bananas","Apple","Orange","Bananas"],
    "Amount":[4,1,2,2,4,5],
    "City":["SF","SF","SF","Montreal","Montreal","Montreal"]
})

df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

df3 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


fig=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color = colors['text']
)

fig2 = px.scatter(df3, x="gdp per capita", y="life expectancy", 
                  size="population", color="continent", hover_name="country", log_x=True, size_max=60)

markdown_text = """
### Dash and Markdown.

Dash app can be writtern in markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown
"""

print(type(fig))
print("===========")
print(generate_table(df2))


app.layout = html.Div(children=[
    html.H1(
          children = "Hello Dash" ,
          style = {
                   'textAlign': 'center',
                   'color':colors['text'] 
                  } ),

    html.Div(
            children="Dash a web application framework for python.",
            style={'textAlign':'center','color':colors['text']}
    ),
    html.Hr(),
    dcc.Graph(
            id='example Graph',
            figure=fig
    ),
    html.Hr(),
    html.H4("US Agriculture Exports (2011)"),
    generate_table(df2),
    html.Hr(),
    dcc.Graph(id="life-exp-vs-gdp",
              figure=fig2
             ),
    html.Hr(),
    dcc.Markdown(children=markdown_text),
    html.Hr(),
    html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
                 options=[
                          {'label':'New york city', 'value':'NYC'},
                          {'label':'Montreal', 'value':'MTL'},
                          {'label':'San Fransisco', 'value':'SF'},
                         ],
                 value='MTL'     
                ),
    html.Hr(),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
                 options=[
                          {'label':'New york city', 'value':'NYC'},
                          {'label':'Montreal', 'value':'MTL'},
                          {'label':'San Fransisco', 'value':'SF'},
                         ],
                 value='MTL',
                 multi=True,     
                ),
    html.Hr(),
    html.Label('Radio Items'),
    dcc.RadioItems(
                  options=[
                          {'label':'New york city', 'value':'NYC'},
                          {'label':'Montreal', 'value':'MTL'},
                          {'label':'San Fransisco', 'value':'SF'},
                   ], value='MTL',
                  ),
    html.Hr(),
    html.Label('Checkboxes'),
    dcc.Checklist(
                options=[
                          {'label':'New york city', 'value':'NYC'},
                          {'label':'Montreal', 'value':'MTL'},
                          {'label':'San Fransisco', 'value':'SF'},
                ], value=['MTL', 'SF'],
    ),
    html.Hr(),
    html.Label("Text Input"),
    dcc.Input(value="MTL", type="text"),
    html.Hr(),
    html.Label("slider"),
    dcc.Slider(min=0, max=10, value=5, marks={i: 'Label {} '.format(i) if i == 1 else str(i) for i in range(0,10)}),
    html.Hr(),
    html.Label("button"),
    html.Button("submit"),
    ], style={'columnCount':3}),
])

if __name__ == '__main__':
    app.run_server(debug=True)

