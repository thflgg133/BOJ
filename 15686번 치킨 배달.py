import sys
from itertools import combinations
chicken_distance = sys.maxsize

N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
house = [] 
chicken_restaurant = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1: # 집일 경우 해당하는 좌표 넣어줌
            house.append([i,j])

        if map[i][j] == 2: # 치킨집일 경우 해당하는 좌표 넣어줌
            chicken_restaurant.append([i,j])

# combinations를 이용해 폐업되지 않고 살아남을 M개의 치킨집의 모든 경우를 구한다
for case in combinations(chicken_restaurant, M): 
    total_distance = 0

    for x, y in house:
        # 각각의 집에서의 치킨거리 총 합을 구한다 
        total_distance += min([abs(x-i[0]) + abs(y-i[1]) for i in case])
       
    if total_distance < chicken_distance:
        chicken_distance = total_distance # 치킨거리의 최솟값을 구한다

print(chicken_distance)