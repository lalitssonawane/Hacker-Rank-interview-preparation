#You are given  queries. Each query is of the form two integers described below:
#-  : Insert x in your data structure.
#-  : Delete one occurence of y from your data structure, if present.
#-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

#The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

from collections import Counter,defaultdict

def freqQuery(queries):
    c = Counter()
    d = defaultdict(set)
    for x,y in queries:
        v = c[y]
        if x==1:
            d[v].discard(y)
            d[v+1].add(y)
            c[y] = v+1
        elif x==3:
            yield 1 if d[y] else 0
        elif v:
            d[v].discard(y)
            d[v-1].add(y)
            c[y] = v-1
            
n = int(input())
queries = [tuple(map(int,input().split())) for i in range(n)]
print(*freqQuery(queries),sep="\n")