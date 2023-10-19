import sys
import heapq
INF = sys.maxsize

# 다익스트라 알고리즘
def dijkstar(start):
    heap = []
    distance[start] = 0 # 시작점의 가중치는 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)
        
        # 최소비용으로 가는 것이 아니면 패스
        if distance[now] < cost:
            continue

        for next_node, weight in graph[now]:
            next_cost = cost + weight

            # 최소 비용으로 가는 것이면 갱신 해줌            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost     
                heapq.heappush(heap, (next_cost, next_node))        


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1) 

# 그래프 생성
for _ in range(M):
    c1, c2, cost = map(int, sys.stdin.readline().split())
    graph[c1].append((c2, cost))    

start, end = map(int, sys.stdin.readline().split())

dijkstar(start)

print(distance[end])