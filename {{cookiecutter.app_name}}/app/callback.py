# -*- coding: utf-8 -*-
"""app/callback.py

Define application callbacks here.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def register_callbacks(app):
    """Wrap the main application function with the application callbacks.

    Multipage apps:
    URL Routing for Multi-Page Apps: https://dash.plot.ly/urls

    """
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/":
            return index.layout
        elif pathname == "/predictions":
            return predictions.layout
        elif pathname == "/insights":
            return insights.layout
        elif pathname == "/process":
            return process.layout
        else:
            return dcc.Markdown("## Page not found")
