import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())

# combinations_with_replacement(iterable, r) : r-길이 튜플들, 정렬된 순서, 반복되는 요소 있음
combi_replace = list(combinations_with_replacement([i for i in range(1,N+1)], M)) 
for i in combi_replace:
    print(*i) # *를 이용해 unpacking