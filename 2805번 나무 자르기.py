import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

low, high = 1 , max(tree) 

while low <= high: # 이분 탐색
    mid = (low + high) // 2 

    total = 0
    for i in tree:
        if i >= mid:
            total += i - mid # 나무를 자르고 가져갈 수 있는 총 길이
            # print(total, mid, high)
    
    if total >= M: # 가져갈 수 있는 총 나무 길이가 M보다 같거나 많을 시
        low = mid + 1 # 더 길게 나무를 잘라야 하므로 low = mid + 1 

    else: # 가져갈 수 있는 총 나무 길이가 M보다 작다면
        high = mid -1 # 더 짧게 나무를 잘라야 하므로 high = mid -1

print(high)