#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from fis3 import FIS
import config


app = Flask(__name__)
app.config.from_object(config)
FIS(app, static_folder=config.FIS_STATIC_FOLDER, template_folder=config.FIS_STATIC_FOLDER, debug=config.FIS_DEBUG)


@app.route('/')
def index():
    return FIS.render_template('page/index/index.html', title='index')


if __name__ == '__main__':
    app.run()

