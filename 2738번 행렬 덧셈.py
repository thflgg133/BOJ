import sys

N, M = map(int, sys.stdin.readline().split())

matrix1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(matrix1[i][j] + matrix2[i][j], end = " ")
        
    print()