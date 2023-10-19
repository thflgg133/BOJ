# 다익스트라
import sys
import heapq
INF = sys.maxsize

def dijkstar(start):
    heap = []
    distance = [INF] * (n+1)
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        wei, now = heapq.heappop(heap)
        
        if distance[now] < wei:
            continue
        
        for next_node, w in graph[now]:
            next_cost = wei + w
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))        

    return distance

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, l))
    graph[b-1].append((a-1, l))

ans = 0  
for i in range(n):
    tmp = 0
    result = dijkstar(i)
    
    for j in range(n):
        if result[j] <= m:
            tmp += items[j]
    
    ans = max(ans, tmp)
    
print(ans)


# 플로이드-와샬
'''
import sys
INF = sys.maxsize

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[INF] * n for _ in range(n)]
print(graph)

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())

    graph[a-1][b-1] = graph[b-1][a-1] = l
    
for k in range(n): # 경유지
    for i in range(n): # 시작점
        for j in range(n): # 끝점
            if i == j:
                graph[i][j] = 0
                
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
ans = 0
for i in range(n):
    tmp = 0 
    for j in range(n):
        if graph[i][j] <= m:
            tmp += items[j]
            
    ans = max(ans, tmp)
    
print(ans)

'''