# -*- coding: utf-8 -*-
"""Main application package."""
import flask
from .dashboard import register_dashboard


def create_app(dashboard):
    """Application factory for the Flask backend serving the dashboard.
    Avoid making changes here unless you are familiar with flask applications.
    """
    app = flask.Flask(__name__)

    register_dashboard(dashboard)

    return app
