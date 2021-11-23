import sys
from collections import deque

def bfs(node):
    queue = deque([node])

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visit_list[i] == 0:
                queue.append(i)
                visit_list[i] = 1 # 방문처리


N, M = map(int, sys.stdin.readline().split())
graph=[[]for i in range(N+1)] 
visit_list=[0] * (N+1) # keypoint 
answer = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    # 서로 연결되어 있음을 보임
    graph[u].append(v) 
    graph[v].append(u) 
    
for i in range(1, N+1):
    if visit_list[i] == 0: # 방문처리 되지 않은 노드에서 bfs()실행 
        bfs(i) # bfs()문을 통해 연결된 노드들은 전부 방문 처리
        answer += 1

print(answer)