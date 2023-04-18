#!/usr/bin/python3
"""Defines a class: Mylist."""


class MyList(list):
    """A child class to a list ."""

    def print_sorted(self):
        """Sorts and print a list in ascending order."""
        print(sorted(self))
