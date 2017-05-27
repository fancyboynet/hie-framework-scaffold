#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from fis3 import FIS


m = Blueprint('m', __name__, url_prefix='/m')


@m.route('/m')
def m_index():
    return FIS.render_template('m:page/index/index.html', title='index')





