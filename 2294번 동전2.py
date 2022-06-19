import sys

n, k = map(int, sys.stdin.readline().split())

cost = [int(sys.stdin.readline()) for _ in range(n)]
dp = [10001] * (k+1)
dp[0] = 0

for i in cost:
    for j in range(i, k+1): # i원 동전의 위치부터 시작 
        dp[j] = min(dp[j], dp[j-i]+1) # 동전의 가치의 배수의 값을 가지면 갱신됨
        
if dp[k] == 10001:
    print(-1)
    
else:
    print(dp[k])