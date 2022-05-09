import sys
from collections import deque


def bfs(i, j):
    cnt = 1
    queue = deque([[i,j]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 방문처리 되지 않은 영역이면 영역 1증가 & 방문처리 후 다시 탐색
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                queue.append([nx, ny])

    return cnt


M, N, K = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 
width = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(y1, y2): # 좌표계 형식이기 때문에 y좌표가 행을 결정한다
        for j in range(x1, x2): # 좌표계 형식이기 때문에 x좌표가 열을 결정한다
            visited[i][j] = 1

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0: # 영역으로 나누어지지 않은 곳 발견시 bfs문 실행
            visited[i][j] = 1
            width.append(bfs(i, j))

print(len(width))
print(*sorted(width))