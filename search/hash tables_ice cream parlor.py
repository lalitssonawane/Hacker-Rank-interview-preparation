#Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

#Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.


from collections import Counter

def icecreamParlor(m, arr):
    costs = Counter(arr)
    half = m/2
    combos = set()
    for cost in costs:
        if (cost!=half and m-cost in costs) or (cost==half and costs[cost]>1):
            combos.add(cost)
    for index,cost in enumerate(arr,1):
        if cost in combos:
            yield index
for _ in range(int(input())):
    m,n = int(input()), int(input())
    arr = list(map(int,(input().split())))
    print(*icecreamParlor(m, arr))