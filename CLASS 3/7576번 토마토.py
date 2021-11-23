import sys
from collections import deque

def tomato():
    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if tomato_box[ny][nx] == 0:
                    tomato_box[ny][nx] = tomato_box[y][x] + 1
                    queue.append((ny, nx))


M, N = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

tomato_box = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
queue = deque()

for y in range(N):
    for x in range(M):
        if tomato_box[y][x] == 1:
            queue.append((y,x))

tomato()
answer = 0
tomato_state = True

for y in range(N):
    for x in range(M):
        if tomato_box[y][x] == 0:
            tomato_state = False
        answer = max(answer, tomato_box[y][x])

if tomato_state == False:
    print(-1)

else:
    print(answer-1)