import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sum_list = [0]

for i in range(N):
    sum_list.append(sum_list[-1] + nums[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sum_list[j])

    else:
        print(sum_list[j]-sum_list[i-1])

