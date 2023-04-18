#!/usr/bin/python3
"""Defines a class: Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Declaring class: Rectangle."""

    def __init__(self, width, height):
        """
        Intializes the Rectangle Class.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return and print str() representation of the Rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
