#!/usr/bin/env python
""" app module
"""
from flask import Flask
from flasck_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/Home/Desktop/side/flask-url-shortener/urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
