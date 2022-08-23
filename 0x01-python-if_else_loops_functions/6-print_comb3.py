#!/usr/bin/python3
for firstLoop in range(0, 10):
    for secondLoop in range(firstLoop+1, 10):
        if firstLoop == 8 and secondLoop == 9:
            print("{}{}".format(firstLoop, secondLoop), end=", ")
