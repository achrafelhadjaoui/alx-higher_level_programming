#!/usr/bin/python3

"""Define a function write_file"""


def write_file(filename="", text=""):
    """a function that write a string to text file
    and return the number of chars written

    Args:
        filename
        text"""

    with open(filename, mode="w", encoding="utf-8") as f:
        write_data = f.write(text)

    return write_data
