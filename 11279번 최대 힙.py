import sys
import heapq

# heapq 모듈을 사용한 풀이

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0 :
        if heap:
            print(heap)
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap, [-x, x])