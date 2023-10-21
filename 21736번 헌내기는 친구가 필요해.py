import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().split())
    campus = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    queue = deque([])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    ans = 0
    
    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                queue.append([i, j])
                break   

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:            
                if campus[nx][ny] == "X":
                    continue
                
                if campus[nx][ny] == "P":
                    ans += 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    
                visited[nx][ny] = True
                queue.append([nx,ny])

    if ans == 0:
        print("TT")
        
    else:
        print(ans)


if __name__ == "__main__":
    main()