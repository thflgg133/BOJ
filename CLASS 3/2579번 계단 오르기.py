import sys

stair = int(sys.stdin.readline())

score = [0]*301
dp = [0]*301

for i in range(stair):
    score[i] = int(input())

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[1] + score[2], score[0] + score[2])

for i in range(3,stair):
    dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i]+dp[i-2])

print(dp[stair-1])