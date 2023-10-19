import sys

N = int(sys.stdin.readline())

max_dp = [[0]*3 for _ in range(2)]
min_dp = [[0]*3 for _ in range(2)]

for i in range(N):
    num_list = list(map(int, sys.stdin.readline().split()))
    
    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + num_list[0]
    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + num_list[0]
    
    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + num_list[1]
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + num_list[1]
    
    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + num_list[2]
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + num_list[2]

    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]

print(max(max_dp[1]), min(min_dp[1]))