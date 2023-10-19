import sys
INF = sys.maxsize

N = int(sys.stdin.readline())
RGB_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = INF

for i in range(3):
    # 미리 처음 집 색깔을 정해두고 시작함
    dp = [[INF]*3 for _ in range(N)]
    dp[0][i] = RGB_cost[0][i]
    
    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + RGB_cost[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + RGB_cost[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + RGB_cost[j][2]
        
    # 처음 집 색깔과 같지 않을때만 유효    
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
       
print(ans)