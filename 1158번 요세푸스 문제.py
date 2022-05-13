import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, N+1)])
ans = ['<']

while queue:
    queue.rotate(-K)
    if len(queue) != 1:
        ans.append(str(queue.pop()) + ',')

    else:
        ans.append(str(queue.pop()))

ans.append('>')

for i in range(len(ans)):
    if i == 0 or i == len(ans)-2:
        print(ans[i], end='')
    
    else:
        print(ans[i], end=' ')