import sys

N = int(sys.stdin.readline())
coordinate = list(map(int, sys.stdin.readline().split()))

sorted_coordinate = sorted(set(coordinate))
sorted_coordinate = {sorted_coordinate[i] : i  for i in range(len(sorted_coordinate))}
print(*[sorted_coordinate[i] for i in coordinate])