import sys
import heapq
INF = sys.maxsize

def dijkstra(start): 
    global cnt 
    
    heap = []
    distance = [INF] * (n+1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    

    while heap:
        cost, now = heapq.heappop(heap)

        for next_node, w in graph[now]:
            next_cost = cost + w
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
  
    if cnt:     
        return distance
    
    else:
        cnt += 1
        return max(dijkstra(now)[1:])
        
        
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
cnt  = 0

# 양방향으로 이동할 수 있으므로 둘다 append
for _ in range(n-1):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

# 1. 루트 노드에서 가장 먼 노드를 찾는다 
# 2. 찾은 노드에서 가장 먼 노드가 트리의 지름이다.
print(dijkstra(1)) # 루트 노드에서 시작