import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    max_heap, min_heap = [], [] 
    visited = [False] * 1000000
    
    k = int(sys.stdin.readline())

    for i in range(k):
        letter, n = sys.stdin.readline().split()

        if letter == 'D':
            if int(n) == -1:
                while min_heap and not visited[min_heap[0][1]]: # min_heap이 빈 heap이 아니면서 visited[min_heap[0][1]] == False 일때 실행
                    heapq.heappop(min_heap)

                if min_heap: # 만약 min_heap 이 빈상태가 아니라면 실행 // 비어 있으면 heappop하면 오류가 뜬다
                    visited[min_heap[0][1]] = False # 상태를 False로 바꿔 줌으로써 나중에 max_heap 에서도 삭제되도록 만듬 -> max_heap 에서는 heappop한 것이 아니므로 
                    heapq.heappop(min_heap)

            elif int(n) == 1:
                while max_heap and not visited[max_heap[0][1]]: # max_heap이 빈 heap이 아니면서 visited[max_heap[0][1]] == False 일때 실행
                    heapq.heappop(max_heap)
                    
                if max_heap:
                    visited[max_heap[0][1]] = False # 상태를 False로 바꿔 줌으로써 나중에 max_heap 에서도 삭제되도록 만듬 -> max_heap 에서는 heappop한 것이 아니므로 
                    heapq.heappop(max_heap)

        if letter == 'I':
            heapq.heappush(max_heap, (-int(n), i)) # max_heap에 n에 -를 붙여서 push함 why? 
                                                   # heappush는 최솟값만 빠져가나는데 D 1 일때 max_heap에서는 최댓값이 pop되야 하므로 n에 -를 붙혀 최솟값을 만들어 pop함
            heapq.heappush(min_heap, (int(n), i)) #  min_heap에 n을 push 함 D -1 일때 최솟값 pop
            visited[i] = True # True면 아직 수가 삭제되지 않고 존재하는 상태 => push했다는 뜻

    while min_heap and not visited[min_heap[0][1]]: heapq.heappop(min_heap) # 걸러져서 False로 바뀐 값들은 버림
    while max_heap and not visited[max_heap[0][1]]: heapq.heappop(max_heap) # 걸러져서 False로 바뀐 값들은 버림

    if min_heap and max_heap: # min_heap 과 max_heap 둘다 빈 heap이 아니라면 최댓값 최솟값 출력
        print(-max_heap[0][0], min_heap[0][0]) # max_heap에 넣을 때 -해주고 넣었으므로 다시 - 붙혀서 출력
    
    else: # 둘 중 하나라도 비었다면 EMPTY 출력
        print('EMPTY')