# -*- coding: utf-8 -*-
"""
Dashboard

"""
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.io as pio

pio.templates.default = 'plotly_white'

colors = {'text': '#329d08'}

# 1. LOAD DATA


df2 = pd.read_csv('country_2018.csv')

df3 = pd.read_csv('country_2018_capita.csv')

df4 = pd.read_csv('21_companies.csv')

df5 = pd.read_csv('100_company_grouped.csv')


# 2. Create figuers for the dashboard

fig_22 = px.treemap(data_frame=df2,
                    values='co2_Gt',
                    path=['country', 'co2_Gt'],
                    labels=None,
                    title= 'Largest 21 countries of the carbon dioxide emissions in gigatons by 2018',
                    color='co2_Gt', 
                    hover_data=['country'],
                    color_continuous_scale='OrRd')

fig_33 = px.treemap(data_frame=df3,
                    values='co2_T',
                    path=['country', 'co2_T'],
                    labels=None,
                    title= 'Biggest 21 countries of the carbon footprint in metric tons per capita by 2018',
                    color='co2_T', 
                    hover_data=['country'],
                    color_continuous_scale='speed')

fig_44 = px.sunburst(df4, 
                     path=['region', 'company'],
                     title='Top 21 contributors to GHG by company that responsible for 50% of total emissions in 2018',
                     values='percent',
                     color='percent',
                     color_continuous_scale='deep',
                     width=1000,
                     height=680,
                     hover_data=['region'])

# 3. Create maps

map_ = px.choropleth(df5, 
                    locations="Alpha-3 code", 
                    color="percent",
                    hover_name="Alpha-3 code", 
                    #animation_frame="percent", 
                    range_color=[0.77,14.32],
                    title="Top 100 companies that cover 70% GHG on the global carbon footprint map in 2018",
                    width=1000,
                    height=680,
                    projection="natural earth")
                    

# 4. INITIALISE THE APP

app= dash.Dash()


# 5. DEFINE THE APP

app.layout = html.Div(children=[
        html.H1(
                children='VISUAL DASHBOARD - explore worldwide carbon dioxide emissions',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'background': 'white'}
    ),
    html.Div(children='''
    Data sources:  ✓ The World Bank  ✓ The Guardian  ✓ The Union of Concerned Scientists
    '''),
     
    dcc.Graph(
        id='example-graph_22',
        figure=fig_22),
    
    dcc.Graph(
        id='example-graph_33',
        figure=fig_33),

    dcc.Graph(
        id='example-graph_44',
        figure=fig_44),
        
    dcc.Graph(
        id='example-graph',
        figure =map_)
])

# 6. RUN THE APP

if __name__ == '__main__':
    app.run_server(debug=True, port=5001)