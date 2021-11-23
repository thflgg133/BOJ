import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

permu =  list(permutations(num_list, M)) #permutations()함수 이용
permu.sort()

for i in permu:
    print(*i) # *를 통해 unpacking