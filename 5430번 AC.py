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
        # cnt가 홀수면 뒤집고, cnt가 짝수면 그대로
        if i == 'R':
            cnt += 1

        elif i == 'D':
            if array:
                # 뒤집어진 상태이기 때문에 원래 배열의 마지막 수를 버림
                if cnt % 2 == 1:
                    array.pop()
                
                # 원래 배열 상태이기 때문에 첫번째 수를 버림
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