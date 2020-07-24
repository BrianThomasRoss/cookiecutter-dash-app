# -*- coding: utf-8 -*-
"""Application entry point definitions."""
import dash
from dash_bootstrap_components.themes import BOOTSTRAP

from .callback import register_callbacks


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

    with server.app_context():
        dashboard.title = "{{cookiecutter.app_name}}"
        register_callbacks(dashboard)

    return dashboard
