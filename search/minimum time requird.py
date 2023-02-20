#You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item. Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.

#For example, you have to produce  items. You have three machines that take.


from math import ceil
from collections import Counter

def minTime(machines, goal):
    c = Counter(machines)
    fastest = min(c)
    min_days = 1
    max_days = ceil((fastest*goal)/c[fastest])
    while max_days-min_days>1:
        mid = (min_days+max_days)//2
        output = sum((mid//x)*y for x,y in c.items())
        if output<goal:
            min_days = mid
        else:
            max_days = mid
    return max_days

n,goal = map(int,input().split())
machines = list(map(int,input().split()))
print(minTime(machines, goal))