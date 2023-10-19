import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)] # N+1개를 만드는 이유? -> 연산을 사용하는 횟수의 최댓값은 1을 빼는 경우로만 이루어질때 이기 떄문이다.

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1 # 1을 빼는 경우 일 때
    if i % 2 == 0 and dp[i] > dp[i//2] + 1: # 2로 나누어 떨어지면 2로 나눈 수 에서 횟수 + 1 
        dp[i] = dp[i//2] + 1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1: # 3으로 나누어 떨어지면 3으로 나눈 수 에서 횟수  + 1
        dp[i] = dp[i//3] + 1

print(dp[N])