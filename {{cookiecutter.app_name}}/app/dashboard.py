# -*- coding: utf-8 -*-
"""Application entry point definitions."""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.callback import register_callbacks
from app.component import navbar, footer


def register_dashboard(server):
    """This function creates the dash application, and conforms to
    the application factory pattern."""
    external_stylesheets = [
        "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",
        "https://use.fontawesome.com/releases/v5.9.0/css/all.css",  # Social Media Icons
    ]
    external_scripts = [
        "https://code.jquery.com/jquery-3.2.1.slim.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
        "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js",
    ]

    meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]

    dashboard = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        meta_tags=meta_tags,
        external_scripts=external_scripts,
        url_base_pathname="/",
        server=server,
    )

    dashboard.layout = html.Div(
        children=[
            dcc.Location(id="url", refresh=False),
            navbar.content,
            dbc.Container(id="page-content", className="mt-4"),
            html.Hr(),
            footer.content,
        ]
    )

    with server.app_context():
        dashboard.title = "my_dash_app"
        register_callbacks(dashboard)

    return dashboard
