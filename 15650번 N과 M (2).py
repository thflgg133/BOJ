import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

combi =  list(combinations([i for i in range(1,N+1)], M)) #combinations()함수 이용
for i in combi:
    print(*i) # *를 통해 unpacking