from collections import deque

N = int(input())
deque =  deque([i for i in range(1,N+1)])
print(deque)

while(len(deque) > 1):
    deque.popleft()
    deque.append(deque.popleft())
    print(deque)

print(deque[0])