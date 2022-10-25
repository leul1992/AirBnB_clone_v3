#!/usr/bin/python3
"""contains app_views blueprint"""
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.users import *


app_views = Blueprint('api', __name__, url_prefix='/api/v1')
