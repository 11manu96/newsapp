#!/Users/ManuMaheshwari/PycharmProjects/newsapp/venv/bin/python

from wsgiref.handlers import CGIHandler
from newsapp import app

CGIHandler().run(app)