#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines class Rectangle"""

    def __init__(self, width, height):
        """ Rectangle class that inherits from BaseGeometry"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area():
        """prints and returns rectangle width and height"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ method for return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
