import sys
from collections import deque

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
                if value == now*2:
                    location[value] = location[now]
                    queue.appendleft(value)

                else:
                    location[value] = location[now] + 1
                    queue.append(value)


N, K = map(int, sys.stdin.readline().split())
limit = 10 ** 5 + 1
location = [-1 for _ in range(limit)]
bfs()