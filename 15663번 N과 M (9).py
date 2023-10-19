import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

# 중복되는 수열 출력을 방지하기 위해 set() 이용
permu = sorted(set(list(permutations(N_list, M))))

for i in permu:
    print(*i)