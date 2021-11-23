import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        if x < 0:
            heapq.heappush(heap, [-x,x])
        
        else:
            heapq.heappush(heap, [x,x])
        
    else: 
        if heap == []:
            print(0)

        else:
            print(heapq.heappop(heap)[1])