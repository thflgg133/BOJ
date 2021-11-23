import sys

N = int(sys.stdin.readline())
RGB_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1,N): # 이전 집 색깔과 겹치지 않는 것이 Key Point
    RGB_cost[i][0] = min(RGB_cost[i-1][1], RGB_cost[i-1][2]) + RGB_cost[i][0] # 빨간색을 색칠하는 비용
    RGB_cost[i][1] = min(RGB_cost[i-1][0], RGB_cost[i-1][2]) + RGB_cost[i][1] # 초록색을 색칠하는 비용
    RGB_cost[i][2] = min(RGB_cost[i-1][0], RGB_cost[i-1][1]) + RGB_cost[i][2] # 파란색을 색칠하는 비용

print(min(RGB_cost[N-1][0], RGB_cost[N-1][1], RGB_cost[N-1][2])) # 색칠한 비용들 중 가장 최소비용을 출력