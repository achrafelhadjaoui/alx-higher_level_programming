#!/usr/bin/python3

"""Define a function read_file"""


def read_file(filename=""):
    """a function that reads a text file and print it to stdout

       Args: filename"""

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data)
