import sys
from collections import deque

def bfs():
    q = deque()
    q.append(N) # 시작점 추가
    
    while q:
        start_point = q.popleft() # 왼쪽에서 뺴는 이유 작은 수 부터 차례대로 조사 해야함 
                                  # 물론 deque를 안쓰고 pop(0)를 이용해 알고리즘을 만들어도 상관없지만 시간복잡도가 증가하기 때문에 비효율
        
        if start_point == K:
            print(location[start_point])
            break
        
        for value in (start_point-1, start_point+1, start_point *2): # 이동할 수 있는 방법 세가지 : -1칸, +1칸, 2배 순간이동 
            if 0 <= value <= limit and location[value] == 0: # 0보다 작은 칸은 존재하지 않으므로 거름 마찬가지로 limit이상의 칸도 존재하지 않으므로 거름, 
                location[value] = location[start_point] + 1 #  keypoint = 원래 위치에서 +! 을 해주므로써 몇초 걸리는지 계속 쌓아갈 수 있음
                q.append(value)


N, K = map(int, sys.stdin.readline().split())
limit = 10**5 # 길이가 100000 이라했으므로 시간절약을 위해 제한생성
location = [0] * (limit+1) # 미리 칸을 만들어서 지정된 칸까지 몇번의 이동이 필요한지 알 수 있도록 도와주는 코드
bfs() # 너비 우선 탐색 함수
print(location[:70])