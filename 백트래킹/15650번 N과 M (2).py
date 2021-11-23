from itertools import combinations

N, M = map(int, input().split())

combi =  list(combinations([i for i in range(1,N+1)], M))
for i in combi:
    print(*i)