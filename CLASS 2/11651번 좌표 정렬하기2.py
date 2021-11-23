import sys

N = int(sys.stdin.readline())
coordinates= []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([y,x]) # y좌표가 증가하는 순서가 먼저이므로 [y,x]를 append함

coordinates.sort() # sort()시 y좌표부터 오름차순으로 우선 정렬되고 그다음에 x좌표가 정렬된다.
for x, y in coordinates:
    print(y,x)