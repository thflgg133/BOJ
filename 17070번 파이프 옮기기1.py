import sys
# 가로= 1, 세로= 2, 대각= 3

# DFS
def dfs(x, y, move):
    global ans
    
    if x == N-1 and y == N-1: # 파이프가 마지막에 도달하면 
        ans += 1
        return
    
    if move == 1 or move == 3: # 파이프가 가로랑 대각선으로 놓여있을때만 가로로 갈 수 있음
        if y+1 < N and map[x][y+1] == 0:
            dfs(x, y+1, 1)
            
    if move == 2 or move == 3: # 파이프가 세로랑 대각선으로 놓여있을때만 세로로 갈 수 있음
        if x+1 < N and map[x+1][y] == 0:
            dfs(x+1 ,y, 2)
            
    if move == 1 or move == 2 or move == 3: # 파이프는 어떤 경우에서도 대각선으로 갈 수 있음
        if x+1 < N and y+1 < N:
            if map[x+1][y] == 0 and map[x][y+1] == 0 and map[x+1][y+1] == 0:
                dfs(x+1 ,y+1 ,3)


N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
dfs(0,1,1)
print(ans)