import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
dp = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + graph[i][j] #구간합을 이용해 해당 인덱스에 해당하는 값을 구한 후 중복으로 더해진 인덱스 값을 빼준다

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1])) # (0,0) ~ (x2,y2) 까지의 구간합들을 다 더하고 겹치는 부분을 뺀 후 중복으로 빼준 구간은 다시 더해준다