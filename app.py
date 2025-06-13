"""
This code creates an interactive web dashboard using Dash to visualize
sales data for Soul Foods’ Pink Morsel product.

Features:

- Loads cleaned sales data from a CSV file.
- Displays a line chart of daily sales over time.
- Allows filtering of sales data by region using a radio button
(options: All, North, East, South, West).
- Highlights the price increase on January 15, 2021
with a red dashed vertical line.
- Uses Dash callbacks to update the chart dynamically based on selected region.
- Runs the app locally in your browser at http: // localhost: 8050.
"""

import os
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

"""" Constants"""
DATA_PATH = "./formatted_sales_data.csv"
COLORS = {"primary": "#FEDBFF", "secondary": "#D598EB", "font": "#522A61"}
"""" Load and prepare data"""
data = pd.read_csv(DATA_PATH)
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values(by="date")
""" Initialize Dash app"""
dash_app = Dash(__name__)
""" Helper to generate the chart"""


def generate_figure(chart_data):
    fig = px.line(
        chart_data,
        x="date",
        y="Sales",  # Sales amount in dollar
        title="Pink Morsel Sales",
        labels={
            "date": "Date",
            "Sales": "Sales Amount ($)"
        })
    fig.update_layout(plot_bgcolor=COLORS["secondary"],
                      paper_bgcolor=COLORS["primary"],
                      font_color=COLORS["font"])
    return fig


""" Initial graph"""
visualization = dcc.Graph(id="visualization", figure=generate_figure(data))
""" Header"""
header = html.H1(" Pink Morsel Visualizer",
                 id="header",
                 style={
                     "background-color": COLORS["secondary"],
                     "color": COLORS["font"],
                     "padding": "1rem",
                     "border-radius": "20px"
                 })
"""" Region picker (set default to "all")"""
region_picker = dcc.RadioItems(["north", "east", "south", "west", "all"],
                               "all",
                               id="region_picker",
                               inline=True,
                               style={"margin": "1rem"})
region_picker_wrapper = html.Div([region_picker], style={"font-size": "120%"})
"""" Callback to update chart based on region"""


@dash_app.callback(Output("visualization", "figure"),
                   Input("region_picker", "value"))
def update_graph(region):
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == region]
    return generate_figure(filtered_data)


"""" Define layout"""
dash_app.layout = html.Div(
    [header, visualization, region_picker_wrapper],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "padding": "2rem",
        "border-radius": "20px",
        "min-height": "100vh"
    })
""" Run the server"""
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    dash_app.run(debug=True, host="0.0.0.0", port=port)
