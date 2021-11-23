import sys

N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1 
    if not i % 2 and dp[i] > dp[i//2] + 1: # 2로 나누어 떨어지면서 & 
        dp[i] = dp[i//2] + 1

    if not i % 3 and dp[i] > dp[i//3] + 1: # 3으로 나누어 떨어지면서 &
        dp[i] = dp[i//3] + 1

print(dp[N])
