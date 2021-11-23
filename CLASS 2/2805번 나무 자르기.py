import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

low, high = 1 , max(tree) 

while low <= high: # 이분 탐색
    mid = (low + high) // 2 

    total = 0
    for i in tree:
        if i >= mid:
            total += i - mid
            # print(total, mid, high)
    
    if total >= M:
        low = mid + 1

    else:
        high = mid -1

print(high)