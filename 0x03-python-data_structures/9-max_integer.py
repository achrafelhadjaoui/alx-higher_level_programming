#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    i = 0
    while i < len(my_list):
        if i == len(my_list) - 1:
            return my_list[i]
        j = i + 1
        while my_list[i] > my_list[j]:
            if j == len(my_list) - 1:
                return my_list[i]
            j += 1
        i = j
