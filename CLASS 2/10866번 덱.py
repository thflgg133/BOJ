from collections import deque
import sys

N = int(sys.stdin.readline())
deque_list = deque([])

for _ in range(N):
    cmd = sys.stdin.readline().split()
    order = cmd[0]

    if order == "push_front":
        deque_list.appendleft(cmd[1])

    if order == "push_back":
        deque_list.append(cmd[1])

    if order == "pop_front":
        if len(deque_list) != 0:
            print(deque_list.popleft()) 

        else:
            print(-1)

    if order == "pop_back":
        if len(deque_list) != 0:
            print(deque_list.pop())
        
        else:
            print(-1)

    if order == "size":
        print(len(deque_list))
    
    if order == "empty":
        if len(deque_list) == 0:
            print(1)

        else:
            print(0)

    if order == "front":
        if len(deque_list) == 0:
            print(-1)

        else:
            print(deque_list[0])
     
    if order == "back":
        if len(deque_list) == 0:
            print(-1)

        else:
            print(deque_list[-1])