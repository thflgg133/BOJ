import sys
from collections import deque

def dfs(graph, start_node):
    queue = deque([start_node])
    visit = []

    while queue:
        node = queue.pop() # 가장 깊숙이 있는 노드부터 탐색해야 하므로

        if node not in visit: # 이미 방문한 노드면 지나감
            visit.append(node)

            if node not in graph:
                return visit

            queue.extend(graph[node])
            
    return visit


def bfs(graph, start_node):
    queue = deque([start_node])
    visit = []

    while queue:
        node = queue.popleft() # 순차적으로 탐색해야 하므로

        if node not in visit: # 이미 방문한 노드면 지나감
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

    graph[key].append(value)
    graph[value].append(key)

for key in graph: # 가장 깊숙이 있는 것 부터 탐색해야하므로 내림차순으로 정렬
    graph[key].sort(reverse=True)      

print(*dfs(graph, V))

for key in graph: # 순차적으로 탐색해야하므로 오름차순으로 정렬
    graph[key].sort()

print(*bfs(graph, V))