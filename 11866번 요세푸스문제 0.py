from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
josephus = [i for i in range(1,N+1)]  #[1,2,3,4,5,6,7]
deq = deque(josephus)
answer = ['<']

while True:
    deq.rotate(-K)
    if len(deq) > 1:
        answer.append(str(deq.pop())+', ')
        cnt += 1

    if len(deq) == 1:
        answer.append(str(deq.pop()))

    if len(deq) == 0:
        answer.append('>')
        break

answer = ''.join(answer)
print(answer)