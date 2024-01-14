#!/usr/bin/python3
i = 97
while i < 123:
    if chr(i) == 'q' or chr(i) == 'e':
        i += 1
    else:
        print("{}".format(chr(i)), end="")
        i += 1
