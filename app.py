import dash
from dash import html, dcc, Input, Output

import dash_auth

#import numpy as np
#import scipy as sp
import pandas as pd
#import seaborn as sns
import plotly.express as px
import id as id
import logic as logic


USERNAME_PASSWORD_PAIRS = [['username', 'password'], [id.username,id.password]]
app = dash.Dash()

#df=pd.read_csv("./Your Career Aspirations of GenZ.csv") 
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
image_path = 'https://pngimg.com/uploads/github/github_PNG48.png'#'./github_PNG48.png'
colors ={'background': '#61D87D','text': '#FFFFFF'}

country = logic.fig_country

gender = logic.fig_gender

job_lasting= logic.fig_joblasting

data_india = logic.data_india

coherence = px.density_heatmap(data_india, x='Your Gender', y= 'How likely would you work for a company whose mission is misaligned with their public actions or even their product ?', text_auto=True)
acc=logic.fig_acc
randfor = logic.fig_rafor_test_eval

app.layout =html.Div([
    html.Div([
    html.H1('GEN-Z', style={'textAlign':'center', 'background':colors['background'], 'color':colors['text']})]),
    html.Hr(),
    html.Div([
    html.A(  # Anchor tag for the link
            href='https://github.com/AlfredoSuarez/ucamp_genz_aitest',  # Replace with your target URL
            target='_blank',  # Open link in a new tab
            children=[
                html.Img(src=app.get_asset_url(image_path), alt='Github Repo Image') #,style={'width': '100px', 'height': '100px'}),  # Image for anchor
            ],
        style={'width': '50%', 'height': '50%'}),
    html.Hr(),
    html.Div([
    html.H2('HR...WHAT WE CAN DO TO RETAIN TALENT?', style={'textAlign':'center', 'backgroundColor':colors['background'], 'color':colors['text']}),

    #dcc.Dropdown(['Account', 'Owner', 'Market'], id='tier1_dropdown')
    #options=[{'label':i, 'value': i} for i in dfdropdown.columns], id='tier1-dropdown'),
    ]),

    html.Hr(),

    dcc.Graph(id='graph_1', figure=country),

    html.Hr(),

    dcc.Graph(id='graph_2', figure=gender),

    html.Hr(),

    dcc.Graph(id='graph_3', figure=coherence),

    html.Hr(),

    dcc.Graph(id='graph_4', figure=job_lasting),

    html.Hr(),

    dcc.Graph(id='graph_5', figure=acc),

    html.Hr(),

    dcc.Graph(id='graph_6', figure=randfor),

    ])])




# In[22]:
if __name__ == '__main__':
    app.run_server(port=8050, debug=False)
