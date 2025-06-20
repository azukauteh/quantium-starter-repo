""" Add test_app.py with basic Dash component tests

Includes tests to verify the presence of:
- Header
- Visualization graph
- Region picker

Uses Dash testing framework with pytest.

"""

from app import dash_app


def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=10)
