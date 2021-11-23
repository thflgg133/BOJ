import sys
import heapq

# heapq 모듈을 사용한 풀이

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0 :
        if heap: # heap이 비어있지 않다면
            print(heapq.heappop(heap)[1]) # heap[1]이 -를 붙히지 않은 원래 값이므로

        else:
            print(0)

    else:
        # heappush는 가장작은 값이 0번째 index로 들어가기때문에 -를 붙혀서 가장 큰 값을 맨 앞에 넣도록 만든다
        heapq.heappush(heap, [-x, x]) 