import sys
from math import sqrt

# 크루스칼 알고리즘
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(x,y):
    root_A = find(A)
    root_B = find(B)

    if root_A < root_B:
        parent[root_B] = root_A

    else:
        parent[root_A] = root_B


n = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
stars = []

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x,y))

edges = []

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edges.sort()
ans = 0

for edge in edges:
    cost, A, B = edge

    if find(A) != find(B):
        union(A, B)
        ans += cost

print(round(ans,2))