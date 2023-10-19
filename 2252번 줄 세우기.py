import sys
from collections import deque

# 위상 정렬
def topology_sort():
    queue = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0: # 들어오는 간선이 없는 노드부터 시작
            queue.append(i)
            ans.append(i)
    
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1 # 간선을 통해 방문했으므로 간선 제거
            
            if indegree[i] == 0:
                queue.append(i)
                ans.append(i)
                
    
    return ans
    

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1
    
ans = []
print(*topology_sort())