import sys
from collections import deque

def check_safe(copy_map): # 안전한 지역을 탐색해서 카운트 해준다
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] == 0:
                cnt += 1
    
    ans.append(cnt)
    

def build_wall(cnt): 
    if cnt == 3: # 벽을 3개 세웠으면 bfs() 실행
        bfs()
        return
    
    # 브루트포스-> map[0][0]부터 3개의 벽을 차례대로 빈 공간일 경우 벽을 세우는 모든 경우를 탐색한다.
    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                map[i][j] = 1
                build_wall(cnt+1)
                map[i][j] = 0 # 모든 경우의 수를 따져야 하므로 세운벽은 다시 빈공간으로 바꿔 줌


def bfs(): 
    # List는 mutable이기 때문에 map의 형태와 같은 List를 하나 더 만들어 for문을 통해 할당해 map과 똑같은 형태로 만들어준다.
    copy_map = [[0]*M for _ in range(N)]
    queue = deque([])

    for i in range(N):
        for j in range(M):
            copy_map[i][j] = map[i][j]
            if copy_map[i][j] == 2: 
                queue.append([i,j]) # 바이러스인 지역은 다시 넣어줘서 계속 퍼져나갈 수 있도록 만든다

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if copy_map[nx][ny] == 0:
                    copy_map[nx][ny] = 2
                    queue.append([nx,ny])

    check_safe(copy_map) # 바이러스가 다 퍼진 후 안전한 지역 탐색


N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []

build_wall(0)
print(max(ans)) # 가장 안전한 지역이 많은 경우 출력