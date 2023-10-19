from collections import deque
import sys

N = int(sys.stdin.readline())
deque_list = deque([])

for _ in range(N):
    cmd = sys.stdin.readline().split()
    order = cmd[0] # 명령어

    if order == "push_front":
        deque_list.appendleft(cmd[1]) # deque에 있는 appendleft() 함수를 이용해 입력받은 수를 왼쪽에 삽입

    if order == "push_back":
        deque_list.append(cmd[1])

    if order == "pop_front":
        if len(deque_list) != 0:
            print(deque_list.popleft()) # deque에 있는 popleft() 함수를 이용해 가장 왼쪽에 있는 수 제거

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