import sys
from collections import deque


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)
  
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)  

            if node not in graph:
                return visit

            stack.extend(graph[node])
            
    return visit


def bfs(graph, start_node):
    visit = list()
    queue = deque()

    queue.append(start_node)

    while queue:
          node = queue.popleft()
          if node not in visit:
            visit.append(node)

            if node not in graph:
                return visit

            queue.extend(graph[node])

    return visit


N, M, V = map(int, sys.stdin.readline().split())
graph = {}

for _ in range(M):
    key, value = map(int, sys.stdin.readline().split())

    if key not in graph:
        graph[key] = []

    if value not in graph:
        graph[value] = []

    graph[key].insert(0, value)
    graph[value].insert(0, key)

for key in graph:
    graph[key].sort(reverse=True)

print(*dfs(graph, V))

for key in graph:
    graph[key].sort()       

print(*bfs(graph, V))