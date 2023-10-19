import sys

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
        
    else:
        parent[x] = y


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

for cnt in range(1,m+1):
    n1, n2 = map(int, sys.stdin.readline().split())
    
    # 부모가 같다는 건 서로 사이클이 형성된다는 뜻
    if find(n1) == find(n2):
        print(cnt)
        exit() # 사이클을 찾았으므로 종료

    # 집합 합치기     
    union(n1, n2)

print(0)