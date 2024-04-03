#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Represent a square"""
    def __init__(self, size):
        """Initialize a new square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self)
        """ area"""
        return self.__size ** 2