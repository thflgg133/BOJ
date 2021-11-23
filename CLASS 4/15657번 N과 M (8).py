import sys
from itertools import combinations_with_replacement, repeat

N, M = map(int, sys.stdin.readline().split())
num_list = sorted(map(int, sys.stdin.readline().split()))

combi_w_replace = list(combinations_with_replacement(num_list, M)) # combinations_with_replacement()함수 이용

for i in combi_w_replace:
    print(*i) # *를 통해 unpacking  