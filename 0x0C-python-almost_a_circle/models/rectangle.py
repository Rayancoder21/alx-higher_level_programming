#!/usr/bin/python3
"""Difinition"""
from models.base import Base


class Rectangle(Base):
    """ Initialize a new Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a new Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
