#!/usr/bin/python3

"""Define a function append_file"""


def append_write(filename="", text=""):
    """a function that append a string at the end to text file
    and return the number of char added

    Args:
        filename
        text"""

    with open(filename, mode="a", encoding="utf-8") as f:
        write_data = f.write(text)

    return write_data
