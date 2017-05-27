#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from fis3 import FIS
import config
from blueprints import www, m

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(www)
app.register_blueprint(m)

FIS(app, static_folder=config.FIS_STATIC_FOLDER, template_folder=config.FIS_STATIC_FOLDER, debug=config.FIS_DEBUG)


if __name__ == '__main__':
    app.run()

