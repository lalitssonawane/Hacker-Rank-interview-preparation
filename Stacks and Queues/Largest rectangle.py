#Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    h += [0]
    s = []
    ma = 0
    for i in range(0, len(h)):
        j = i
        while len(s) > 0 and s[-1][0] >= h[i]:
            val, j = s.pop()
            ma = max(ma, (i - j) * val)
        s.append([h[i], j])
    return ma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()