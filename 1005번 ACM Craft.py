import sys
from collections import deque

# 위상 정렬
def topology_sort():
    queue = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0: # 들어오는 간선이 없는 노드부터 시작
            queue.append(i)
            dp[i] = construct_time[i-1]

    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1 # 간선을 통해 방문했으므로 간선 제거
            dp[i] = max(dp[now] + construct_time[i-1], dp[i])
            
            if indegree[i] == 0:
                queue.append(i)
                
    return dp[W]


T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    
    construct_time = list(map(int, sys.stdin.readline().split()))
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    dp = [0 for _ in range(N+1)] 
    
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1
        
    W = int(sys.stdin.readline())
    
    print(topology_sort())