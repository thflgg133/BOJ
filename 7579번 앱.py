import sys

N, M = map(int, sys.stdin.readline().split())
bytes = [0] + list(map(int, sys.stdin.readline().split()))
costs = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)]
ans = sum(costs)

for i in range(1, N+1):
    for j in range(1, sum(costs)+1):
        if costs[i] > j: #  cost가 부족하여 앱을 끌 수 없으므로 계속 활성화
            dp[i][j] = dp[i-1][j]
            
        else:
            dp[i][j] = max(dp[i-1][j - costs[i]] + bytes[i], dp[i-1][j])
        
        # 가장 최소의 비용으로 M 메모리 이상을 확보하는 비용 구하기    
        if dp[i][j] >= M:
            ans = min(ans, j)
          
if M != 0:
    print(ans)
    
else:
    print(0) 