#!/usr/bin/env python3
"""models.py
        - This module contains the URL class
"""
from app import db


class URL(db.Model):
    """URL class
    """
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(100), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)

    def __repr__(self):
        """__repr__ method"""
        return f"URL('{self.original_url}', '{self.short_url}', '{self.visits}')"
