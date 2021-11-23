import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(N) # 시작점
    location[N][0] = 0
    location[N][1] = 1
    
    while queue:
        now = queue.popleft()
           
        for value in (now-1, now+1, now*2):
            if 0 <= value < limit:
                if location[value][0] == -1: # 처음 방문 했을 때
                    location[value][0] = location[now][0] + 1
                    location[value][1] = location[now][1]
                    queue.append(value) # 이동한 위치에서 다시시작
            
                elif location[value][0] == location[now][0] + 1: # 처음 방문하는게 아닐 때
                    location[value][1] += location[now][1] # 경우의 수 더함


N, K = map(int, sys.stdin.readline().split())
limit = 10 ** 5 + 1
location = [[-1,0] for _ in range(limit)]
bfs()
print(location[K][0])
print(location[K][1])