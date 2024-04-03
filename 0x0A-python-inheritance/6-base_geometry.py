#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """ Represent base geometry."""
    def area(self):
        """ method for calculated area"""
        raise Exception("area() is not implemented")
