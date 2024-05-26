#!/usr/bin/env python3
""" app.py 
    - The main entry point for the application.
    - This script runs the Flask application.
"""
from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
