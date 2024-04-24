# app/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'events.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
