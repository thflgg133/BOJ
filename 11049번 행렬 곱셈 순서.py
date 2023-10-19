import sys
INF = 2**32

N = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(1, N): # 자신의 행렬과 차이나는 칸의 거리, 0일때는 자기자신과 곱하므로 어차피 0이라 생략 
    for j in range(N-i): # 해당 행렬을 기준으로 탐색
        if i == 1: # 자기자신과 한칸 차이나는 칸은 그냥 곱하면 됨
            dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+1][1]
            continue

        dp[j][j+i] = INF # 가장 최악의 경우의 값 미리 할당  

        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

print(dp[0][N-1])