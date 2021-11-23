import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
dp = [1] * N # Dynamic Programming 이용ㅇ

for i in range(N):
    for j in range(i):
        if N_list[i] > N_list[j]:
            dp[i] = max(dp[i], dp[j]+1) # dp[현재 인덱스], dp[현재 이전의 인덱스]+1 값을 비교하여 더 큰 값 할당 

print(max(dp))