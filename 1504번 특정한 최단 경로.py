import sys
import heapq
INF = sys.maxsize

def dijkstra(start):
    heap = []
    distance = [INF] * (N+1)
    distance[start] = 0
    heapq.heappush(heap, (0, start)) # (가중치, 노드)
    
    while heap:
        cost, now = heapq.heappop(heap)
        
        if distance[now] < cost:
            continue
        
        for next_node, w in graph[now]:
            next_cost = cost + w
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
    
    return distance


N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))  

v1, v2 = map(int, sys.stdin.readline().split())

original = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# 시작 -> v1 -> v2 , 시작 -> v2 -> v1 중 최단경로를 구함
result = min(original[v1] + v1_distance[v2] + v2_distance[N],
             original[v2] + v2_distance[v1]+ v1_distance[N])

print(result if result < INF else -1)