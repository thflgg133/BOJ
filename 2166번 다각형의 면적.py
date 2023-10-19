import sys

N = int(sys.stdin.readline())

coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinates.append(coordinates[0])
wide = 0

# 신발끈정리 공식을 이용해 면적의 넓이 구함 
for i in range(N):
    wide += (coordinates[i][0] * coordinates[i+1][1]) - (coordinates[i][1] * coordinates[i+1][0])
    
print(round(abs(wide)/2, 1))