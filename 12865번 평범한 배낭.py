import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
stuff = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        wei = stuff[i][0]
        value = stuff[i][1]

        if j < wei:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(value + dp[i-1][j-wei], dp[i-1][j])

print(dp[N][K])