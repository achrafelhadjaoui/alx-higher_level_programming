#!/usr/bin/python3

"""Define Class MyList that inherits from list"""


class MyList(list):
    """Represent of MyList"""

    def print_sorted(self):
        """method that sorted in a list"""
        print(sorted(list(self)))
