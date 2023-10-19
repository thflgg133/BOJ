import sys
from collections import deque

def maze_serach(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque([[0,0]]) # 시작점


    while queue: # queue가 빌 때까지
        x, y = queue.popleft() 

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 0: # 0이면 이동 할 수 없기 떄문에 패스
                    continue    
                
                elif maze[nx][ny] == 1: # 1인 곳은 갈 수 있지만 아직 방문 안한 곳
                    maze[nx][ny] = maze[x][y] + 1 # maze index에 각 이동횟수 표시
                    queue.append([nx, ny]) # queue에 인덱스 값을 넣어서 다시 그 인덱스부터 진행되도록 만듬

    return maze[N-1][M-1]
    

N, M= map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
      maze.append(list(map(int, sys.stdin.readline().rstrip())))

print(maze_serach(0,0))