import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split()))
    imp = deque(map(int, sys.stdin.readline().split()))
    idx = deque(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 가장 앞에 있는 문서의 중요도 확인
        if imp[0] == max(imp):
            order += 1
                        
            # 가장 앞에 있는 문서의 중요도가 가장 높고 찾으려는 target 일 때
            if idx[0] == 'target':
                print(order)
                break

            else:
                imp.popleft()
                idx.popleft()

        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())   