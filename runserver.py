#!/usr/bin/env python

from os import environ
environ['METAREFRESH_ENV'] = 'development'

from paystation import app
from paystation.models import db

db.create_all()
app.run('0.0.0.0', 6200, debug=True)
