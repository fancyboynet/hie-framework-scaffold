#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from fis3 import FIS


www = Blueprint('www', __name__)


@www.route('/')
def index():
    return FIS.render_template('www:page/index/index.html', title='index')





