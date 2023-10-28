#!/usr/bin/python3
"""A module to handle the blueprints"""

from flask import Flask, Blueprint
from api.v1.views import *

app_views = Blueprint(url_prefix='/api/v1')