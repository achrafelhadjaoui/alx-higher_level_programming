#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for row in sorted(a_dictionary.keys()):
        print("{}: {}".format(row, a_dictionary[row]))
