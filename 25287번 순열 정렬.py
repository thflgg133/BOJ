import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    state = True
    tmp = min(arr[0], N - arr[0] + 1)
    
    for i in range(1, N):
        max_num = min(arr[i], N - arr[i] + 1)
        min_num = max(arr[i], N - arr[i] + 1)  