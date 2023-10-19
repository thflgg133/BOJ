import sys

# bfs
def bfs(x,y):
    global ans
    
    queue = set([(x,y,alphabet[0][0])])
    
    while queue:
        x, y, char_list = queue.pop()
        
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C and alphabet[nx][ny] not in char_list:
                queue.add((nx, ny, char_list+alphabet[nx][ny]))
                ans = max(ans, len(char_list)+1)
        
        
R, C = map(int, sys.stdin.readline().split())
alphabet = [sys.stdin.readline().rstrip() for _ in range(R)]
ans = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs(0,0)
print(ans)


'''
import sys

# 백트래킹, 아스키코드
def dfs(x,y,cnt):
    global ans
    
    ans = max(ans, cnt)
    
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and char_dict[ord(alphabet[nx][ny])] is False:
            char_dict[ord(alphabet[nx][ny])] = True
            dfs(nx,ny,cnt+1)
            char_dict[ord(alphabet[nx][ny])] = False
 
        
R, C = map(int, sys.stdin.readline().split())
alphabet = [sys.stdin.readline().rstrip() for _ in range(R)]
char_dict = [False for i in range(ord('Z')+1)] 
char_dict[ord(alphabet[0][0])] = True
ans = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dfs(0,0,1)
print(ans)
'''