#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set()
    for row in set_1:
        for row_1 in set_2:
            if row == row_1:
                new_set.add(row)

    return new_set
