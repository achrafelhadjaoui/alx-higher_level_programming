#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """check if the list is not empty"""
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
