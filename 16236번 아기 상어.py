import sys
import heapq

def bfs():
    visited = [[False] * N for _ in range(N)]
    shark_size = 2
    exp = 0
    ans = 0
    
    while heap:
        cnt, x, y = heapq.heappop(heap)
        
        # 해당 칸의 물고기를 먹을 수 있을 때
        if 0 < space[x][y] < shark_size:
            exp += 1
            space[x][y] = 0
            
            if shark_size == exp:
                shark_size += 1
                exp = 0
                
            ans += cnt
            cnt = 0
            
            # 상어의 크기가 커지면 새롭게 먹을 수 있는 칸이 생기므로 초기화
            visited = [[False] * N for _ in range(N)]
            while heap:
                heap.pop()
            
        # 해당 칸의 물고기를 먹을 수 없다면 방향 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 아기상어보다 크기가 큰 물고기는 먹을 수 없으므로 지나감
            if 0 <= nx < N and 0 <= ny < N:
                if space[nx][ny] > shark_size or visited[nx][ny]:
                    continue
                
                # 먹을 수 있다면 걸린 시간과 인덱스 값을 heap에 넣어줌
                heapq.heappush(heap, (cnt+1, nx, ny))
                visited[nx][ny] = True
                
    return ans

N = int(sys.stdin.readline())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heap = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            # heap은 첫번째 원소를 기준으로 우선순위가 결정되므로 시간을 맨 앞에 배치
            heapq.heappush(heap, (0, i, j))
            space[i][j] = 0
            break
        
print(bfs())