#!/usr/bin/python3
"""Defines a class: Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Declaring a class: Square."""

    def __init__(self, size):
        """
        Initializing Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
