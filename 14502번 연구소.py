import sys
from collections import deque

def check_safe(copy_map): # 0인 지역을 탐색해서 카운트 해준다
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] == 0:
                cnt += 1
    
    ans.append(cnt)
    

def build_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    # 브루트포스-> map[0][0]부터 3개의 벽을 차례대로 빈 공간일 경우 벽을 세우는 모든 경우를 탐색한다.
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                build_wall(cnt+1)
                maps[i][j] = 0


def bfs(): 
    # List는 mutable이기 때문에 deepcopy를 사용하여 원래의 map형태가 변하지 않게 만들어 준다.
    copy_map = [[0]*M for _ in range(N)]
    queue = deque([])

    for i in range(N):
        for j in range(M):
            copy_map[i][j] = maps[i][j]
            if copy_map[i][j] == 2: 
                queue.append([i,j]) # 바이러스인 지역은 다시 넣어줘서 계속 퍼져나갈 수 있도록 만듬

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if copy_map[nx][ny] == 0:
                    copy_map[nx][ny] = 2
                    queue.append([nx,ny])

    check_safe(copy_map)


N, M = map(int, sys.stdin.readline().split())
maps = [list(maps(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []

build_wall(0)
print(max(ans)) # 가장 안전한 지역이 만은 경우 출력