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
        
'''
heapq 모듈

import heapq

heapq.heappush(heap, parameter) -> heap 에 parameter값 append
heapq.heappop(heap) -> heap 안에 최솟값 제거 및 그 다음 최솟값이 heap[0]에 위치할 수 있도록 수정
heapq.heapify(heap) -> 기존 리스트를 힙으로 변환
'''