import sys

N = int(sys.stdin.readline())
coordinates = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([x,y])

coordinates.sort() # x, y 좌표에 대해 오름차순으로 정렬
for x, y in coordinates:
    print(x,y)