import sys
from collections import deque


def maze_serach(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((x,y)) # (0,0) -> 시작점

    while queue: # queue가 빈 큐가 될때까지
        x, y = queue.popleft() # pop(0) 는 시간복잡도 증가하므로 deque 사용

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치범위 설정 미로를 벗어나는 값은 오류나기 때문에 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
      
            if maze[nx][ny] == 0: # 0이면 이동 할 수 없기 떄문에 패스
                continue    
      
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # maze index에 각 이동횟수 표시
                queue.append((nx, ny)) # queue에 인덱스 값을 넣어서 다시 그 인덱스에서 진행되도록 만듬

    return maze[N-1][M-1] # 리스트 인덱스 값이라 -1씩 해줘야 함
    

N, M= map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
      maze.append(list(map(int, sys.stdin.readline().rstrip())))

print(maze)
print(maze_serach(0,0))