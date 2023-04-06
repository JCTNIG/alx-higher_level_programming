#!/usr/bin/python3
"""Sets a locked class: LockedClass"""


class LockedClass:
    """prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name."""

    __slots__ = ["firist_name"]
