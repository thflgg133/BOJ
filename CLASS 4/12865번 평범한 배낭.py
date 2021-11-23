import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
stuff = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, sys.stdin.readline().split())))

# Knapsack Algorithm -> 표 형태로 만들어 해결함
for i in range(1, N+1):
    for j in range(1, K+1):
        wei = stuff[i][0] 
        value = stuff[i][1]

        if j < wei: # 현재 물건의 무게가 기입하려는 무게 보다 크다면 이전 무게의 총 가치를 그대로 가져온다.
            dp[i][j] = dp[i-1][j]

        else:
            # max(현재 물건의 가치 + 현재 물건을 넣기 전의 가치, 같은 무게일때 다른 물건들을 넣었을때의 가치)
            dp[i][j] = max(value + dp[i-1][j-wei], dp[i-1][j]) #

print(dp[N][K])