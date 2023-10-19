import sys
from collections import deque

def dfs(): # 깊이 우선 탐색 활용
    queue = deque([1]) # 트리의 루트가 1번이므로 1번 노트부터 시작

    while queue: # 트리에 연결된 노드들을 전부 탐색
        node = queue.popleft()
        
        for i in graph[node]:
            if not visited[i]: # 방문하지 않은 노드일때 
                # queue에 다시 넣어줘서 넣어준 노드부터 다시 탐색 될 수 있도록 함
                queue.append(i) 
                # queue에 넣어준 노드의 부모노드는 현재 노드와 같음
                parent[i] = node
                # 이미 방문한 노드는 다시 탐색할 필요가 없기 때문에 방문처리를 함
                visited[i] = True 


N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs()
print(*parent[2:], sep="\n") # 2번 노드부터 부모 노드 출력