#!/usr/bin/env python3
"""routes.py
        - This module contains the routes for the app
"""
from flask import Blueprint, render_template, request, redirect, flash
from app.models import URL, db
import string
import random

main = Blueprint('main', __name__)

def generate_short_url():
    """Generates a random short URL
    """
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for i in range(6))
    if URL.query.filter_by(short_url=short_url).first():
        return generate_short_url()
    return short_url

@main.route('/')
def index():
    """Index route
    """
    return render_template('index.html')

@main.route('/shorten_url', methods=['POST'])
def shorten_url():
    """Shorten URL route
    """
    original_url = request.form['original_url']
    url = URL.query.filter_by(original_url=original_url).first()
    if url:
        short_url = url.short_url
    else:
        short_url = generate_short_url()
        url = URL(original_url=original_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()

    return render_template('index.html', shortened_url=url.short_url)

@main.route('/<short_url>')
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
