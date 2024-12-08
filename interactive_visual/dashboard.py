import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output


df = pd.read_csv("spacex.csv")
unique_launch_sites = list(df["Launch Site"].unique())
max_mass = max(df["Payload Mass (kg)"])
dd_options = [
                {"label": site, "value": site} for site in (unique_launch_sites)
                    ]
dd_options.append({'label': 'All Sites', 'value': 'ALL'})
app = dash.Dash(__name__)                    
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output


df = pd.read_csv("spacex.csv")
unique_launch_sites = list(df["Launch Site"].unique())
max_mass = max(df["Payload Mass (kg)"])
dd_options = [
                {"label": site, "value": site} for site in (unique_launch_sites)
                    ]
dd_options.append({'label': 'All Sites', 'value': 'ALL'})
app = dash.Dash(__name__)                    
app.layout = html.Div(
    children=[html.H1('Airline Performance Dashboard', 
                style={'textAlign': 'center', 'color': '#503D36',
                'font-size': 40}),
                html.Div(["Input Year: ", dcc.Dropdown(
                id="launch-sites",
                options=dd_options,
                value='ALL',
                placeholder="All sites",
                searchable = True
                )],
                style={'font-size': 20}),
                html.Br(),
                html.Br(),
                html.Div(dcc.Graph(id='success-pie-chart')),
                html.Div(["Choose mass: ",
                          dcc.RangeSlider(id='payload-slider',
                                        min=0, max=10000, step=1000,
                                        marks={0: '0',
                                               2500: '2500',
                                               5000: "5000",
                                               9600: "%s" % str(max_mass),},
                                               
                                        value=[min(df["Payload Mass (kg)"]), max(df["Payload Mass (kg)"])])], style={'font-size': 20}),
                html.Div(dcc.Graph(id='success-scatter-chart')),
                ],)


# add callback decorator
# @app.callback(Output(component_id='success-pie-chart', component_property='figure'),
#               Input(component_id='launch-sites', component_property='value'))
# # Add computation to callback function and return graph
# def get_graph(site):
    
#     if site == 'ALL':
#         data = df
#         fig = px.pie(data, values='class', 
#         names=df["Launch Site"], 
#         )
#         fig.update_layout(title='All sites success rate')
#         return fig
    
#     else:
#         selected_data = df[df["Launch Site"] == site]
#         fig = px.pie(selected_data,
#                      names='class'
#         )
#         fig.update_layout(title=f'{site} success rate')
#         return fig



@app.callback([Output(component_id='success-pie-chart', component_property='figure'),
               Output(component_id='success-scatter-chart', component_property='figure')],
              [Input(component_id='launch-sites', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_graph1(site, payload):
    if site == 'ALL':
        
        fig1 = px.pie(df, values='class', 
               names=df["Launch Site"], 
                        )
        
        data = df[df["Payload Mass (kg)"] <= payload[1]]
        data = data[data["Payload Mass (kg)"] >= payload[0]]
        fig2 = px.scatter(data, x='Payload Mass (kg)', 
        y='class',
        color='Booster Version'
        )
        fig1.update_layout(title='All sites success rate')
        return fig1, fig2
    
    else:
        selected_data = df[df["Launch Site"] == site]
        fig1 = px.pie(selected_data,
                     names='class'
        )
        fig1.update_layout(title=f'{site} success rate')
        
        selected_data = selected_data[selected_data["Payload Mass (kg)"] <= payload[1]]
        selected_data = selected_data[selected_data["Payload Mass (kg)"] >= payload[0]]
        fig2 = px.scatter(selected_data, x='Payload Mass (kg)', 
        y='class',
        color='Booster Version' 
        )
        
        return fig1, fig2

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=9000)
app.layout = html.Div(
    children=[html.H1('Airline Performance Dashboard', 
                style={'textAlign': 'center', 'color': '#503D36',
                'font-size': 40}),
                html.Div(["Input Year: ", dcc.Dropdown(
                id="launch-sites",
                options=dd_options,
                value='ALL',
                placeholder="All sites",
                searchable = True
                )],
                style={'font-size': 20}),
                html.Br(),
                html.Br(),
                html.Div(dcc.Graph(id='success-pie-chart')),
                html.Div(["Choose mass: ",
                          dcc.RangeSlider(id='payload-slider',
                                        min=0, max=10000, step=1000,
                                        marks={0: '0',
                                               2500: '2500',
                                               5000: "5000",
                                               9600: "%s" % str(max_mass),},
                                               
                                        value=[min(df["Payload Mass (kg)"]), max(df["Payload Mass (kg)"])])], style={'font-size': 20}),
                html.Div(dcc.Graph(id='success-scatter-chart')),
                ],)


# add callback decorator
# @app.callback(Output(component_id='success-pie-chart', component_property='figure'),
#               Input(component_id='launch-sites', component_property='value'))
# # Add computation to callback function and return graph
# def get_graph(site):
    
#     if site == 'ALL':
#         data = df
#         fig = px.pie(data, values='class', 
#         names=df["Launch Site"], 
#         )
#         fig.update_layout(title='All sites success rate')
#         return fig
    
#     else:
#         selected_data = df[df["Launch Site"] == site]
#         fig = px.pie(selected_data,
#                      names='class'
#         )
#         fig.update_layout(title=f'{site} success rate')
#         return fig



@app.callback([Output(component_id='success-pie-chart', component_property='figure'),
               Output(component_id='success-scatter-chart', component_property='figure')],
              [Input(component_id='launch-sites', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_graph1(site, payload):
    if site == 'ALL':
        
        fig1 = px.pie(df, values='class', 
               names=df["Launch Site"], 
                        )
        
        data = df[df["Payload Mass (kg)"] <= payload[1]]
        data = data[data["Payload Mass (kg)"] >= payload[0]]
        fig2 = px.scatter(data, x='Payload Mass (kg)', 
        y='class',
        color='Booster Version' 
        )
        fig1.update_layout(title='All sites success rate')
        return fig1, fig2
    
    else:
        selected_data = df[df["Launch Site"] == site]
        fig1 = px.pie(selected_data,
                     names='class'
        )
        fig1.update_layout(title=f'{site} success rate')
        
        selected_data = selected_data[selected_data["Payload Mass (kg)"] <= payload[1]]
        selected_data = selected_data[selected_data["Payload Mass (kg)"] >= payload[0]]
        fig2 = px.scatter(selected_data, x='Payload Mass (kg)', 
        y='class',
        color='Booster Version' 
        )
        
        return fig1, fig2

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=9000)