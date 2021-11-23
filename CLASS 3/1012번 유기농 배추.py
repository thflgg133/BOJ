import sys
sys.setrecursionlimit(10000) # 파이썬에서 기본 재귀의 깊이의 제한은 1000이므로 임위로 늘려줘야 한다

def dfs(x,y):
    dir = [[0,1],[0,-1],[1,0],[-1,0]] # 방향설정

    for diff in dir:
        dx = x + diff[1] # 1 -1 0 0
        dy = y + diff[0] # 0 0 1 -1

        if (0 <= dx < N) and (0 <= dy <M):
            if field[dx][dy] == 1:
                field[dx][dy] = 0 
                dfs(dx,dy)


for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0 for i in range(M)] for i in range(N)]
    cnt = 0

    for _ in range(K):
        diff_x, diff_y = map(int, sys.stdin.readline().split())
        field[diff_y][diff_x] = 1

    for i in range(N): # 행
        for j in range(M): # 열
            if field[i][j] == 1:
                dfs(i,j)
                cnt += 1 # 탐색이 종료되면 지렁이 한마리 추가
            
    print(cnt)