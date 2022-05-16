import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split()))) # enumerate함수를 통해 인덱스 할당
ans = []

# rotate() 함수 양수는 오른쪽, 음수는 왼쪽으로 회전
while queue:
    num, target = queue.popleft()
    ans.append(num+1) 
    if target > 0:
        queue.rotate(-(target-1))
        
    else:
        queue.rotate(-target)
 
print(*ans)