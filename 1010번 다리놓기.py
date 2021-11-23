import sys
from math import factorial

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    print(factorial(M) // (factorial(M-N) * factorial(N))) # 조합(Combination)개념 이용