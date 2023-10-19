import sys

n = int(sys.stdin.readline())
dp = [0] * 1001 # n은 최대 1000까지 이므로 1001개 생성(0번째 포함)
# n == 2일때 까지는 규칙성이 보이지 않으므로 따로 생성
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = dp[i-1] + (dp[i-2] * 2) # n>=3 일때 다음과 같은 규칙이 성립된다

print(dp[n] % 10007)