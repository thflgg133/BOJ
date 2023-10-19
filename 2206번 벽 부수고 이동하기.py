import sys
from collections import deque

def bfs():
    queue = deque([[0,0,0]])
    visited[0][0][0] = 1
    
    while queue: 
        # state : 0 -> 벽을 부시지 않은 상태, state : 1 -> 벽을 부순 상태
        x, y, state = queue.popleft() 
        
        if x == N-1 and y == M-1:
            return visited[x][y][state]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 부시지 않은 상태면 벽을 한번 뚫고 지나갈 수 있다
                if map[nx][ny] == 1 and state == 0:
                    # 벽을 부순 상태로 넘어가고 움직인 거리 갱신
                    queue.append([nx, ny, state+1])
                    visited[nx][ny][state+1] = visited[x][y][state] + 1
                       
                # 움직일 수 있지만 아직 방문하지 않은 칸        
                if map[nx][ny] == 0 and visited[nx][ny][state] == 0:
                    # 움직인 거리 갱신
                    queue.append([nx,ny,state])
                    visited[nx][ny][state] = visited[x][y][state] + 1
                                      
    return -1   


N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

print(bfs())