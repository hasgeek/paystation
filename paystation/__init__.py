#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Website server for PayStation.
"""

from flask import Flask
from flask.ext.assets import Environment, Bundle
from baseframe import baseframe, baseframe_js, baseframe_css
#from os import environ
from coaster.app import configure

# First, make an app and config it

app = Flask(__name__, instance_relative_config=True)
configure(app, 'METAREFRESH_ENV')

app.register_blueprint(baseframe)
assets = Environment(app)
js = Bundle(Bundle(baseframe_js,  'js/jquery.smooth-scroll.min.js', 'js/paystation.js',
                   filters='jsmin', output='js/paystation-packed.js'),
            'js/leaflet/leaflet.js')
css = Bundle(Bundle(baseframe_css, 'css/paystation.css', 'css/responsive.css',
                    filters='cssmin', output='css/paystation-packed.css'),
             'js/leaflet/leaflet.css')
assets.register('js_all', js)
assets.register('css_all', css)

import paystation.views
#if environ.get('PAYSTATION_ENV') == 'prod':
#    import paystation.loghandler
