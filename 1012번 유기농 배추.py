import sys
sys.setrecursionlimit(2500)

def dfs(x,y):
    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    for diff in dir:
        dx = x + diff[1] # 1 -1 0 0
        dy = y + diff[0] # 0 0 1 -1

        if (0 <= dx < N) and (0 <= dy <M):
            if field[dx][dy] == 1:
                field[dx][dy] = 0
                dfs(dx,dy)

T = int(input())
for _ in range(T):
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
                cnt += 1 
            
    print(cnt)