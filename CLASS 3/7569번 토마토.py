import sys
from collections import deque

def tomato():
    while queue:
        z, y, x = queue.popleft() # 순차적으로 발견된 익은 토마토에서 부터 시작, 한번 실행되면 popleft()를 통해 중복 실행되지 않도록 함

        for i in range(6):
            nx = x + dx[i] # x좌표 설정
            ny = y + dy[i] # y좌표 설정
            nz = z + dz[i] # z좌표 설정

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H: # 박스 안 범위에서 돌도록 하는 조건
                if tomato_box[nz][ny][nx] == 0: # 토마토가 들어있지 않은 곳 과 익은 곳은 pass
                    tomato_box[nz][ny][nx] = tomato_box[z][y][x] + 1 # 몇번에 걸쳐 익은 토마토가 되는지 알 수 있게 해주는 코드 
                    queue.append((nz,ny,nx))                         # 굳이 익은 토마토를 1로 만들 필요가 없다 X     
                    # 익은 토마토가 된 좌표들을 새롭게 queue에 넣어줌

M, N, H = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0, 0, 0] # x축 방향
dy = [0, 0, 1, -1, 0, 0] # y축 방향
dz = [0, 0, 0, 0, 1, -1] # z축 방향

tomato_box = [[list(map(int, sys.stdin.readline().split())) for i in range(N)] for i in range(H)] # 농장 형성
queue = deque() # 시간복잡도 줄이기 위해 deque() 사용

for z in range(H): # z축
    for y in range(N): # y축
        for x in range(M): # x축
            if tomato_box[z][y][x] == 1: # 익은 토마토 발견시 queue에 index값들 추가
                queue.append((z,y,x))  

tomato() # tomato 함수 실행
answer = 0
tomato_state = True 

for z in range(H): # z축
    for y in range(N): # y축
        for x in range(M): # x축
            if tomato_box[z][y][x] == 0:
                tomato_state = False # 익지 않은 토마토가 있을 시 False 할당
            answer = max(answer, tomato_box[z][y][x]) # max함수를 사용해 tomato_box안에 가장 큰 값 찾기
                                                 
if tomato_state == False: # tomato_box안에 0인 값이 발견 된다면 익지 않은 토마토가 존재하는 것이므로 -1 출력
    print(-1)

else:
    print(answer-1) # 처음부터 1이라고 두고 시작했으니 answer-1 해줘야함                