#Karl loves playing games on social networking sites. His current favorite is CandyMaker, where the goal is to make candies.

#Karl just started a level in which he must accumulate  candies starting with  machines and  workers. In a single pass, he can make  candies. After each pass, he can decide whether to spend some of his candies to buy more machines or hire more workers. Buying a machine or hiring a worker costs  units, and there is no limit to the number of machines he can own or workers he can employ.

#Karl wants to minimize the number of passes to obtain the required number of candies at the end of a day. Determine that number of passes.



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    days = 0
    candies = 0
    answer = math.ceil(n / (m * w))

    while days < answer:
        if p > candies:
            daysNeeded = math.ceil((p - candies) / (m * w))
            candies += daysNeeded * m * w
            days += daysNeeded

        diff = abs(m - w)
        available = candies // p
        purchased = min(diff, available)

        if m < w:
            m += purchased
        else:
            w += purchased

        rest = available - purchased
        m += rest // 2
        w += rest - rest // 2
        candies -= available * p

        candies += m * w
        days += 1

        remainingCandies = max(n - candies, 0)
        answer = min(answer, days + math.ceil(remainingCandies / (m * w)))
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()