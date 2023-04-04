#!/usr/bin/python3
"""Defination of class: Rectangle"""


class Rectangle:
    """Initialising class: Rectangle"""
    def __init__(self, width=0, height=0):
        """intialising Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute: width"""
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter for private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute: height"""
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >=0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
