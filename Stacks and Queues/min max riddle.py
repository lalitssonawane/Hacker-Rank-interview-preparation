#Given an integer array of size , find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.




#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    n = len(arr)
    max_mins = [None]*n
    stack = [] # will store (num, index)
    for i in range(n):
        #print('stack', stack)
        #print('max_mins', max_mins)
        # remember to "push back"
        _m = i
        while len(stack) > 0 and stack[-1][0] > arr[i]:
            _v, _i = stack.pop(-1)
            w = i - _i
            for _w in range(w): # note that it's zero indexed and shifted down
                if max_mins[_w] is None:
                    max_mins[_w] = _v
                else:
                    max_mins[_w] = max(max_mins[_w], _v)
            _m = _i # get the smallest index at which we could start
        stack.append((arr[i],_m))

    # these were the minima for all this time
    while len(stack) > 0:
        #print('stack', stack)
        #print('max_mins', max_mins)
        _v, _i = stack.pop(-1)
        w = n - _i
        for _w in range(w):
            if max_mins[_w] is None:
                max_mins[_w] = _v
            else:
                max_mins[_w] = max(max_mins[_w], _v)
    return max_mins

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
