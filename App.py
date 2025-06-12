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
- Runs the app locally in your browser at http://localhost:8050.
"""


import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px


class PinkMorselApp:
    def __init__(self):
        """Initialize the Dash app"""
        self.app = dash.Dash(__name__)
        self.df = self._load_data()
        self._configure_layout()
        self._register_callbacks()

    def _load_data(self):
        """Load and process the formatted sales data"""
        df = pd.read_csv("formatted_sales_data.csv")
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
        return df

    def _create_figure(self, region):
        """Create a line chart filtered by region, with a vertical line"""
        if region != "all":
            filtered_df = self.df[self.df["region"] == region]
        else:
            filtered_df = self.df

        fig = px.line(
            filtered_df,
            x="date",
            y="Sales",
            color="region",
            title="Pink Morsel Sales Over Time",
            labels={"date": "Date", "Sales": "Sales Amount (R)"}
        )

        fig.add_vline(
            x=pd.to_datetime("2021-01-15"),
            line_dash="dash",
            line_color="red",
            annotation_text="Price Increase",
            annotation_position="top left"
        )

        return fig

    def _configure_layout(self):
        """Define the app layout"""
        self.app.layout = html.Div(style={"fontFamily": "Arial",
                                          "padding": "20px"}, children=[
            html.H1("🧁 Pink Morsel Sales Visualiser",
                    style={"color": "#D6336C"}),

            html.Div([
                html.Label("Select Region:", style={"fontWeight": "bold"}),
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    labelStyle={"display": "inline-block",
                                "margin-right": "15px"}
                )
            ], style={"marginBottom": "20px"}),

            dcc.Graph(id="sales-line-chart")
        ])

    def _register_callbacks(self):
        """Define the callback for interactivity"""
        @self.app.callback(
            Output("sales-line-chart", "figure"),
            Input("region-selector", "value")
        )
        def update_figure(selected_region):
            return self._create_figure(selected_region)

    def run(self):
        """Run app on localhost"""
        self.app.run_server(debug=True, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    PinkMorselApp().run()
