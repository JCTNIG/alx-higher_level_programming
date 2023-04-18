#!/usr/bin/python3
"""
defines the MyList class
"""


class MyList(list):
    """a child class of list"""
    def __init__(self):
        """object initializing Mylist class"""
        super().__init__()

    def print_sorted(self):
        """sorts and prints sorted list in ascending other"""
        print(sorted(self))
