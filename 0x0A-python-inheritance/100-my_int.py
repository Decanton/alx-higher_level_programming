#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""

class MyInt(int):
    """Custom integer class with inverted == and != operators"""

    def __eq__(self, other):
        """Inverted equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted inequality operator"""
        return super().__eq__(other)

