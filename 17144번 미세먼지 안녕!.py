import sys
from copy import deepcopy

# 미세먼지 확산
def spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    tmp_maps = [[0]*C for _ in range(R)]
    tmp_maps[air_up][0], tmp_maps[air_down][0] = -1, -1
    
    for row in range(R):
        for col in range(C): 
            if house[row][col] > 0:
                cnt = 0
                
                for i in range(4):
                    nx = row + dx[i]
                    ny = col + dy[i]

                    if 0 <= nx < R and 0 <= ny < C and house[nx][ny] != -1:
                        tmp_maps[nx][ny] += house[row][col] // 5
                        cnt += 1
                
                tmp_maps[row][col] += house[row][col] - house[row][col] // 5 * cnt

    return tmp_maps


# 위쪽 공기청정기 (반시계방향 순환)
def up(): 
    tmp_maps = deepcopy(house)
    # 오른쪽 -> 위쪽 -> 왼쪽 -> 아래쪽
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    x, y = air_up, 1 # 시작점
    print(house)
    house[x][y] = 0
    print(house)
    
    for i in range(4):
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx == air_up and ny == 0:
                print(house)
                return
            
            if 0 <= nx < R and 0 <= ny < C:
                house[nx][ny] = tmp_maps[x][y]
                
            else:
                break
            
            x, y = nx, ny


# 아래쪽 공기청정기 (시계방향 순환)      
def down(): 
    tmp_maps = deepcopy(house)
    # 오른쪽 -> 아랫쪽 -> 왼쪽 -> 위쪽
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = air_down, 1 # 시작점
    house[x][y] = 0
    
    for i in range(4):
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx == air_down and ny == 0:
                return
            
            if 0 <= nx < R and 0 <= ny < C:
                house[nx][ny] = tmp_maps[x][y]
             
            else:
                break
           
            x, y = nx, ny


R, C, T = map(int, sys.stdin.readline().split())

house = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기청정기 위치 찾기
for i in range(R):
    if house[i][0] == -1:
        air_up = i
        air_down = i+1
        break
    
for _ in range(T):
    house = spread()
    up()
    down()

house[air_up][0], house[air_down][0] = 0, 0

answer = 0
for i in range(R):
    for j in range(C):
        if house[i][j] > 0:
            answer += house[i][j]

print(answer)