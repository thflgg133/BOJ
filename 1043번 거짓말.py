import sys

# Union - find
def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x,y): 
    x, y = find(x), find(y)
    if x != y:
        parent[y] = parent[x]


N, M = map(int, sys.stdin.readline().split())
truth = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N+1)]
party = []

for i in range(truth[0]):
    union(truth[1], truth[i+1])
    
for j in range(M):
    num, *people_list = map(int, sys.stdin.readline().split())
    party.append(people_list)
    
    if num > 1:
        for cur in range(num-1):
            union(people_list[cur], people_list[cur+1])
            
ans = 0
for people in party:
    for cur in range(len(people)):
        if len(truth) > 1 and find(people[cur]) == find(truth[1]):
            ans += 1
            break
        
print(M-ans)