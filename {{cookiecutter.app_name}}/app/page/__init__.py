# -*- coding: utf-8 -*-
"""app/page

This module contains individual page layouts. To add a page to the
dashboard create the new page <PAGE-TITLE>.py, define the layout, and
add it to __all__, and the list of imports. Then follow
"""
__all__ = ["index", "insights", "predictions", "process"]

from . import index, insights, predictions, process

def render_page(app):
    app.layout = html.Div(
        [
            dcc.Location(id="url", refresh=False),
            navbar,
            dbc.Container(id="page-content", className="mt-4"),
            html.Hr(),
            footer,
        ]
    )

