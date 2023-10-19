import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(N):
    for j in range(N):
        # dp[i][j] 번째는 2번 더해지니까 한번 뺴줘야 한다
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + graph[i][j]

# 누적 합이므로 중복되는 값들을 빼준다 dp[x1-1][y1-1]은 2번 빼지니까 한번 더해줘야 한다.
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))