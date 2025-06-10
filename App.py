"""
This code creates a web dashboard using Dash to visualize
sales data for Soul Foods’ Pink Morsel product.

It does the following:

- Loads cleaned sales data from a CSV file.
- Displays a line chart of daily sales over time, grouped by region.
- Highlights the date when the price increased — January 15, 2021
 — with a red dashed line.
- Runs the app locally in your browser at http://localhost:8050.
"""

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


class PinkMorselApp:
    def __init__(self):
        """Initialize the Dash app"""
        self.app = dash.Dash(__name__)
        self._configure_layout()

    def _load_data(self):
        """Load and process the formatted sales data"""
        df = pd.read_csv("formatted_sales_data.csv")
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
        return df

    def _create_figure(self, df):
        """Create a line chart and add a vertical line
             on the price change date"""
        df["date"] = df["date"].astype(str)

        fig = px.line(
            df,
            x="date",
            y="Sales",
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
        """Load data, create figure, and define app layout"""
        df = self._load_data()
        fig = self._create_figure(df)

        self.app.layout = html.Div(children=[
            html.H1("🧁 Pink Morsel Sales Visualiser"),
            dcc.Graph(id="sales-line-chart", figure=fig)
        ])

    def run(self):
        """Run app on localhost"""
        self.app.run(debug=True, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    PinkMorselApp().run()
