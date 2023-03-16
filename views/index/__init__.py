#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:__init__.py.py
# author:ZCJ
# datetime:2022/6/24 19:32
# software: PyCharm

"""
this is function  description 
"""

from flask import Blueprint

index_bp = Blueprint('index', __name__)

from . import indexviews
