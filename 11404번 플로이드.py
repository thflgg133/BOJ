import sys
INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
maps = [[INF] * n for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    
    if cost < maps[start-1][end-1]:
        maps[start-1][end-1] = cost

for k in range(n): # 경유지
    for i in range(n): # 시작점
        for j in range(n): # 끝점
            if i == j:
                maps[i][j] = 0
                
            else:
                maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])
                
for i in range(n):
    for j in range(n):
        print(0 if maps[i][j] == INF else maps[i][j], end = " ")   
    print()