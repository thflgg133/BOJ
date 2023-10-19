import sys
import heapq # 작은 번호의 노드부터 순서대로 탐색하기 위해 사용
INF = sys.maxsize

# 다익스트라 알고리즘
def dijkstra(start): 
    heap = []
    distance[start] = 0 # 시작점의 가중치는 0
    heapq.heappush(heap, (0, start)) # (가중치, 노드)

    while heap:
        cost, now = heapq.heappop(heap)
      
        if distance[now] < cost: # 똑같은 노드로 이동하는데 가중치가 최소가 아니라면 패스
            continue

        for next_node, weight in graph[now]:
            next_cost = cost + weight # 다음노드로 갔을 때의 가중치 = 현재가중치 + 다음노드를 가기 위해 필요한 가중치
      
            # 다음 노드로 가는 가중치가 현재 가중치보다 작다면 갱신
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node)) # 노드 이동 후 다시 현재 노드와 지금까지 쌓인 가중치를 다시 heap에 넣어줌


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
distance = [INF] * (V+1)    
graph = [[] for _ in range(V + 1)]


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split()) # u -> v (가중치 = w)
    graph[u].append((v,w))

dijkstra(K)

for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])