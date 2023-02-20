#Determine the minimum cost to provide library access to all citizens of HackerLand. There are  cities numbered from  to . Currently there are no libraries and the cities are not connected. Bidirectional roads may be built between any city pair listed in . A citizen has access to a library if:

#Their city contains a library.
#They can travel by road from their city to a city containing a library.


#!/bin/python3

def dfs(graph, start, visited):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

def roadsAndLibraries(n, cLib, cRoad, cities):
    # construct graph as adjacency-list
    graph = {i: set() for i in range(1,n+1)}
    for city1, city2 in cities:
        graph[city1].add(city2)
        graph[city2].add(city1)

    # if libraries are cheaper than roads, build 
    #   library in every city and build no roads
    if cLib < cRoad:
        return cLib * n

    # determine number of connected components (CC) in graph
    visited = set()
    nCC = 0
    for city in range(1, n+1):
        if city not in visited:
            dfs(graph, city, visited)
            nCC += 1

    # 1 library per CC, nCitiesPerCC-1 roads per CC
    return nCC*cLib + (n-nCC)*cRoad

if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        n, m, cLib, cRoad = map(int, input().split())
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().split())))

        result = roadsAndLibraries(n, cLib, cRoad, cities)
        print(result)