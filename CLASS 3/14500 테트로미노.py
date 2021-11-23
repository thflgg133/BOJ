import sys

def block(i, j):
    global answer

    for x in range(19):
        result = 0
        for y in range(4):
            try:
                next_x = i + tetromino[x][y][0] # X좌표
                next_y = j + tetromino[x][y][1] # Y좌표
                result += paper[next_x][next_y]            
            except IndexError: # 인덱스가 범위를 벗어날때 패스
                continue 

            answer = max(answer, result)

N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# ㅁ으로 1가지, ㅡ로 2가지, ㄴ으로 8가지, ㅜ 으로 4가지, 나머지 모양으로 4가지 => 총 19 가지
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], 
    [(0,0), (0,1), (0,2), (0,3)], 
    [(0,0), (1,0), (2,0), (3,0)], 
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], 
    [(0,0), (0,1), (0,2), (1,2)], 
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], 
    [(1,0), (1,1), (1,2), (0,1)], 
    [(0,0), (1,0), (2,0), (1,1)], 
    [(1,0), (0,1), (1,1), (2,1)], 
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

answer = 0
for i in range(N):
    for j in range(M):
        block(i, j)

print(answer)