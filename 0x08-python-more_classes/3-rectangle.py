#!/usr/bin/python3
"""
Defination of class: Rectangle
"""


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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute: height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """area of class: Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of class: Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """printable string of class: Rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
