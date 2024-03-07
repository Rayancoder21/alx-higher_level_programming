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

    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y
