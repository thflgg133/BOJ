import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x > 0 :
        heapq.heappush(heap, x)

    elif x == 0:
        if heap == []:
            print(0)

        else:
            print(heap[0])
            heapq.heappop(heap)