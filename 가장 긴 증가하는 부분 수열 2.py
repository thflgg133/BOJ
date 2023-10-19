import sys
import bisect

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

# Dynamic Programming 이용
dp = [N_list[0]]

# 앞 쪽 기준
for i in range(N):
    if N_list[i] > dp[-1]:
        dp.append(N_list[i])

    else:
        # 이분탐색을 이용해 logN 의 복잡도로 이전의 가장 큰 원소의 idx값을 찾는다.
        idx = bisect.bisect_left(dp, N_list[i])
        dp[idx] = N_list[i]

print(len(dp))