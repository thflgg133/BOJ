import sys
from collections import deque

def bfs():
    queue = deque([N])
    
    while queue:
        now = queue.popleft() # 왼쪽에서 뺴는 이유 작은 수 부터 차례대로 조사 해야함 
                                      
        if now == K:
            print(location[now])
            break
        
        for value in (now-1, now+1, now *2): # 이동할 수 있는 방법 세가지 : -1칸, +1칸, 2배 순간이동 
            if 0 <= value <= limit and not location[value]: # 0보다 작은 칸과 limit이상의 칸은 존재하지 않으므로 pass
                # keypoint = 원래 위치에서 +1 을 해서 해당위치 까지 몇초만에 도달할 수 있는 지 파악
                location[value] = location[now] + 1 
                # print(location[:K+1]) -> 칸 이동수 검증
                queue.append(value) # 위치 갱신


N, K = map(int, sys.stdin.readline().split())
limit = 10**5 # 길이가 100000 이므로 시간절약을 위해 제한생성
location = [0] * (limit+1) # 미리 칸을 만들어서 지정된 칸까지 몇번의 이동이 필요한지 알 수 있도록 한다.
bfs() 