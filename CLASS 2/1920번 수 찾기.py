import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

for i in M_list: 
    low, high = 0, N-1  
    target = i  # M_list 안에 있는 수를 target으로 설정
    answer = 0
    while low <= high: # 이분 탐색 알고리즘,  시간복잡도 : O(log N)
        mid = (low + high) // 2 # 범위를 계속 반으로 줄여나가면서 탐색한다. mid가 홀수 일때를 방지하기 위에 몫만 사용
        if N_list[mid] == target: 
            answer = 1
            break
               
        elif target < N_list[mid]: # target이 N_list[mid]보다 작다면 그 보다 작은 범위 안에 있이므로 high = mid - 1로 설정 
            high = mid - 1 

        else:
            low = mid + 1 # target이 N_list[mid]보다 크다면 그 보다 큰 범위 안에 있이므로 low = mid + 1로 설정

    print(answer) # low <= high 동안 if문을 만족하지 못한다면 그대로 0 