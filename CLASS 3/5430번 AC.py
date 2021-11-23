import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    array = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    if n == 0:
        array = deque()

    state = True
    cnt = 0

    for i in p:
        if i == 'R':
            cnt += 1

        elif i == 'D':
            if array:
                if cnt % 2 == 1:
                    array.pop()
                
                else:
                    array.popleft()

            else:
                print("error")
                state = False
                break

    if state:
        if cnt % 2 == 1:
            array.reverse()
            print("[" + ",".join(array) + "]")

        else:
            print("[" + ",".join(array) + "]")