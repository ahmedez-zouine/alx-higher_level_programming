#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if j != 9 or i != 9:
            print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:d}{:d}".format(i, j))
