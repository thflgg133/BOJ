import sys

K, N = map(int, sys.stdin.readline().split())
lan_lines = [int(sys.stdin.readline()) for _ in range(K)]
low, high = 0, 10000000000

while low <= high: # 이분 탐색 -> 시간복잡도 O(logN) 
    mid = (low + high) // 2
    num = 0

    for lan in lan_lines: 
        num += (lan // mid) # 각각의 랜선을 설정한 값으로 나눈 몫을 num에 더함

    if num >= N: # 만약 num이 만드려는 개수 N개보다 크거나 같다면 더 큰 값으로 나눠야하므로 mid+1을 low값으로 다시 설정한다
        low = mid + 1 # +1을 하지 않고 low = mid 로 하면 항상 low <= high 이므로 while문을 벗어날 수 없다

    else:  # 만약 num이 만드려는 개수 N보다 작다면 더 작은 값으로 나눠야하므로 mid-1을 high값으로 다시 설정한다
        high = mid - 1 # -1을 하지 않고 low = mid 로 하면 항상 low <= high 이므로 while문을 벗어날 수 없다

print(high)