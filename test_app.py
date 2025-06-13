 """test_app.py"""

import pytest
from dash.testing.application_runners import import_app


@pytest.mark.usefixtures("dash_duo")
def test_header_is_present(dash_duo):
    app = import_app("app")  # import app from app.py
    dash_duo.start_server(app.dash_app)

    header = dash_duo.find_element("#header")
    assert header.text == "Pink Morsel Visualizer"


@pytest.mark.usefixtures("dash_duo")
def test_visualization_is_present(dash_duo):
    app = import_app("App")
    dash_duo.start_server(app.dash_app)

    graph = dash_duo.find_element("#visualization")
    assert graph is not None


@pytest.mark.usefixtures("dash_duo")
def test_region_picker_is_present(dash_duo):
    app = import_app("App")
    dash_duo.start_server(app.dash_app)

    radio = dash_duo.find_element("#region_picker")
    assert radio is not None

