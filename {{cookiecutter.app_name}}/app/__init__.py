# -*- coding: utf-8 -*-
"""Main application package."""
import flask
from app.dashboard import register_dashboard


def create_app():
    """Application factory for the Flask backend serving the dashboard.
    Avoid making changes here unless you are familiar with flask applications.
    """
    app = flask.Flask(__name__)

    register_dashboard(app)

    return app
