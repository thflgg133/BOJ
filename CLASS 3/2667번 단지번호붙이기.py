import sys

# 굳이 모든 구역을 예시처럼 1구역, 2구역 ,3구역으로 만들 필요는 없다!
# 생각의 전환 -> 그냥 0으로 만들어주면서 아파트 개수만 세주면 되는것!
# 총 단지수는 answer의 길이

def house_map(x,y):
    global cnt
    house[x][y] = '0' # 들어온 house[x][y] == 1 이므로 0 으로 만들어주면서 바로 cnt 값 증가시킴
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
    
        if house[nx][ny] == '1':
            house_map(nx, ny) # 4방향중에 '1'이 있으면 이어갈 수 있으니 재귀함수로 계속 반복

            
N = int(sys.stdin.readline())
house = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
answer = []

for i in range(N):
    for j in range(N):
        if house[i][j] == '1':
            cnt = 0
            house_map(i,j)
            answer.append(cnt)

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])