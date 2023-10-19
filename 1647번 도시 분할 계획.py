import sys

# 크루스칼 알고리즘
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        
    return parent[x]


def union(a, b):
    root_A = find(a)
    root_B = find(b)
    
    if root_A < root_B:
        parent[root_B] = root_A
    
    else:
        parent[root_A] = root_B
        

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append((C, A, B))
  
graph.sort()
  
parent = [i for i in range(N+1)]
result = 0
max_cost = 0
cnt = 0

for i in range(M):
    C, A, B = graph[i]
    
    if find(A) != find(B):
        union(A, B)
        cnt += 1
        result += C
        max_cost = C

        # MST가 구해지면 종료
        if cnt == N-1:
            break
        
# 가장 비용이 큰 길만 제거하면 마을이 2개로 나누어짐
print(result - max_cost)