import sys
from collections import deque

'''
# 실패한 코드
def bfs():
    queue = deque([N])
    location[N][0] = 0
    location[N][1] = True

    while queue:
        now = queue.popleft()

        if now == K:
            print(location[now][0])
            break

        for value in (now*2, now-1, now+1):
            if 0 <= value < limit:
                if location[value][1] == True:
                    pass

                elif value == now*2:
                    location[value][0] = location[now][0]
                    location[value][1] = True
                    queue.append(value)

                else:
                    location[value][0] = location[now][0] + 1
                    queue.append(value)

N, K = map(int, sys.stdin.readline().split())
limit = 10 ** 5 + 1
cnt = 0
location = [[-1, False] for _ in range(limit)]
bfs()
'''


# 성공한 코드
def bfs():
    queue = deque([N])
    location[N] = 0

    while queue:
        now = queue.popleft()

        if now == K:
            print(location[now])
            break

        for value in (now*2, now-1, now+1):
            if 0 <= value < limit and location[value] == -1:
                if value == now*2: # 순간이동 할 때
                    location[value] = location[now]
                    queue.appendleft(value)

                else: # 좌, 우로 갈 떄
                    location[value] = location[now] + 1
                    queue.append(value)


N, K = map(int, sys.stdin.readline().split())
limit = 10 ** 5 + 1
location = [-1 for _ in range(limit)]
bfs()