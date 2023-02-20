#The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.

#Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, determine the minimum time to stop the attack.

class Edge(object):
    def __init__(self, city1: int, city2: int, weight: int):
        self.cities = [city1, city2]
        self.weight = weight

[N, K] = [int(i) for i in input().split(' ')]
edges = list()
for i in range(N - 1):
    line = input()
    #print(line)
    [city1, city2, weight] = [int(j) for j in line.split(' ')]
    edges.append(Edge(city1, city2, weight))

edges.sort(key = lambda x: x.weight, reverse = True)

cityToGroup = dict()
machineCities = dict()
for i in range(K):
    mc = int(input())
    machineCities[mc] = True
    cityToGroup[mc] = mc
    
result = 0
groups = dict()
for i in range(N):
    groups[i] = [i]
    cityToGroup[i] = i

for e in edges:
    city1 = e.cities[0]
    city2 = e.cities[1]
    g1 = cityToGroup[city1]
    g2 = cityToGroup[city2]
    if g1 == g2:
        continue
    if machineCities.get(g1, None) is not None: # in this group we have a machine
        if machineCities.get(g2, None) is not None: # do not add this edge, as it connects the machines
            result += e.weight
        else:
            for c in groups[g2]:
                cityToGroup[c] = g1
                groups[g1].append(c)
            del groups[g2]
    else: # Either the second group has a machine or not, we add all g1 cities to it and delete the first g1
        for c in groups[g1]:
            groups[g2].append(c)
            cityToGroup[c] = g2
        del groups[g1]
print(result)
