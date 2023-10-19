from re import L
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
dp = [[0 for _ in range(N)] for _ in range(N)]

for section in range(N):
    for start in range(N-section):
        end = start + section

        # 숫자 하나는 무조건 팰린드롬 수
        if start == end:
            dp[start][end] = 1

        elif nums[start] == nums[end]:
            # 길이가 2일때 시작 숫자와 끝 숫자가 같다면 팰린드롬 수
            if start+1 == end:
                dp[start][end] = 1

            # 문자열 가운데가 팰린드롬 수 이면 팰린드롬 수 
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1


for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S-1][E-1])