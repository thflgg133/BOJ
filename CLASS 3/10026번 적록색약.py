import sys
from collections import deque 
sys.setrecursionlimit(10000) # recursion error 때문에 범위를 제한함 N <= 100이므로 N x N = 10000 이다.

def bfs(i, j ):
    queue.append([i,j])
    visited[i][j] = True # 방문한 영역은 True
    color = RGB_pic[i][j]

    while queue: 
        i, j = queue.popleft() # 방문한 영역 노드는 제거
        
        for dir in range(4): # 현재 영역에서 상하좌우 탐색
            nx = i + dx[dir] 
            ny = j + dy[dir]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False and RGB_pic[nx][ny] == color: # 방문하지 않은 영역 + 탐색을 시작한 영역이랑 색깔이 같다면 bfs탐색 반복
                    queue.append([nx,ny]) # 새로 방문한 노드는 queue에 다시 추가
                    bfs(nx, ny)


N = int(sys.stdin.readline())
RGB_pic = [list(sys.stdin.readline().rstrip()) for _ in range(N)] # RGB 영역 생성
visited = [[False] * N for _ in range(N)] # RGB 영역 중 방문한 영역을 표시하기 위해 만듬
queue = deque()

dx = [1, -1, 0, 0] # x축 방향 설정
dy = [0, 0, 1, -1] # y축 방향 설정
RGB_cnt, RB_cnt = 0, 0

# 일반적인 사람이 RGB_pic을 볼 때 구분하는 색의 영역
for i in range(N):
    for j in range(N):
        if visited[i][j] == False: # 방문하지 않은 영역이면 bfs탐색  
            bfs(i, j)
            RGB_cnt += 1 

# 적록색약인 사람이 RGB_pic을 볼때 R,G 구분을 못하기 때문에 한 색깔로 통일
for i in range(N):
    for j in range(N):
        if RGB_pic[i][j] == "G":
            RGB_pic[i][j] = "R"

visited = [[False] * N for _ in range(N)] # 다시 영역 초기화

 # 적록색약인 사람이 RGB_pic을 볼 때 구분하는 색의 영역           
for i in range(N):
    for j in range(N):
        if visited[i][j] == False: # 방문하지 않은 영역이면 bfs탐색
            bfs(i, j)
            RB_cnt += 1

print(RGB_cnt, RB_cnt)