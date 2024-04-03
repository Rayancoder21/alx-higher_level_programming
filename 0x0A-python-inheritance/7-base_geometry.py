#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """ Represent base geometry."""

    def area(self):
        """ method for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if type(value) not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError({} must be greater than 0.format(name))
