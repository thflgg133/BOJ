import sys


def bfs():
    pass







N = int(sys.stdin.readline())
fishing_port = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if fishing_port[i][j] == 9:
            bfs()

            