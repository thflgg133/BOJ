import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()


for i in M_list:
    low, high = 0, N-1 # N - 1 == 2
    target = i # [1,3,7,9,5]
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if N_list[mid] == target:
            answer = 1
            break
            
        elif target < N_list[mid]:
            high = mid -1

        else:
            low = mid +1

    print(answer)