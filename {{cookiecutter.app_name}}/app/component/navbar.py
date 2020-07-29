# -*- coding: utf-8 -*-
"""
Application navigation bar.

Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
"""
import dash_html_components as html
import dash_bootstrap_components as dbc

content = html.Div(
    [
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Learn More", header=True),
                        dbc.DropdownMenuItem("Process", href="/process"),
                        dbc.DropdownMenuItem("Predictions", href="/predictions"),
                        dbc.DropdownMenuItem("Insights", href="/insights"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="More",
                ),
            ],
            brand="{{cookiecutter.project_name}}",
            brand_href="/",
            color="primary",
            dark=True,
        )
    ]
)
