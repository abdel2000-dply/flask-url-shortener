#!/usr/bin/env python
"""routes.py
        - This module contains the routes for the app
"""
from flask import render_template, request, redirect, flash
from app import app, db
from models import URL
import string
import random


def generate_short_url():
    """Generates a random short URL
    """
    chars = string.ascii_letters + string.digits
    # chars equal to 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    short_url = ''.join(random.choice(chars) for i in range(6))
    if URL.query.filter_by(short_url=short_url).first():
        return generate_short_url()
    return short_url


@app.route('/')
def index():
    """Index route
    """
    return render_template('index.html')


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    """Shorten URL route
    """
    original_url = request.form['original_url']
    short_url = generate_short_url()
    url = URL(original_url=original_url, short_url=short_url)
    db.session.add(url)
    db.session.commit()

    return render_template('shorten_url.html', short_url=short_url)


@app.route('/<short_url>')
def redirect_to(short_url):
    """Redirect route
    """
    url = URL.query.filter_by(short_url=short_url).first()
    if url:
        url.visits += 1
        db.session.commit()
        return redirect(url.original_url)
    flash('Invalid URL')
    return redirect('/')
