#!/usr/bin/python3
""" Defines a square class"""
from models.rectangle import Rectangle


class square(Rectangle):
    """ Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return the print() and str() representation of a Square."""
        return "[Square]({}) {}/{} {}".format(self.id, self.x, self.y, self.width)
