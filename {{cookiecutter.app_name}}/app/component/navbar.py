# -*- coding: utf-8 -*-
"""
Application navigation bar.

Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
"""
import dash_core_components as dcc
import dash_bootstrap_components as dbc

header = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="{{cookiecutter.project_name}}",
    brand_href="#",
    color="primary",
    dark=True
)
