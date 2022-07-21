import sys
import heapq

# pypy3 제출
'''
N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heap = []

for current in arr:
    if not heap: # heap이 비어있을 경우
        for i in current:
            heapq.heappush(heap, i)
            
    else: # heap이 비어있지 않을 경우
        for i in current:
            if heap[0] < i:
                # heap의 0번째 인덱스를 N번째 수로 유지시키기 위해
                # heappush를 한 후 heappop을 통해 N번째 수 보다 작은 값의 수를 제거시킨다.
                heapq.heappush(heap, i)
                heapq.heappop(heap)
                
print(heap[0])
'''

# python3 제출
N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
        
    if not heap:       
        for i in arr:
            heapq.heappush(heap, i)
     
    else:
        for i in arr:
            if heap[0] < i:
                heapq.heappush(heap, i)
                heapq.heappop(heap) 
                
print(heap[0])