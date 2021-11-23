from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
josephus = deque([i for i in range(1,N+1)]) # deque로 선언 rotate() 함수를 쓰기 위해
answer = ['<']

while True:
    josephus.rotate(-K) # 왼쪽으로 K만큼 이동 0번째 인덱스는 마지막 인덱스로 이동한다]
    if len(josephus) > 1:
        answer.append(str(josephus.pop()) + ', ')  # -K만큼 이동시켜서 K번째 사람을 제거시킨다.
    
    if len(josephus) == 1: # josephus안에 값이 1개인 경우는 > 가 붙어서 출력되어야 하므로 따로 설정
        answer.append(str(josephus.pop()) + '>')
        break

answer = ''.join(answer)
print(answer)