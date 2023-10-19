import sys

N = int(sys.stdin.readline())

path = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#플로이드-워셜 알고리즘
for k in range(N): # 경유지
    for i in range(N): # 시작점
        for j in range(N): # 끝점
            if path[i][k] and path[k][j]:
                path[i][j] = 1

for row in path: # 행
    for col in row: # 열
        print(col, end = " ")
    print()