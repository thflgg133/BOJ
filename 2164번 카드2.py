import sys
from collections import deque

N = int(sys.stdin.readline())
deque =  deque([i for i in range(1,N+1)]) 

while(len(deque) > 1):
    deque.popleft() # 카드에서 가장위에 있는 수 버림
    deque.rotate(-1) # rotate()함수를 이용해 deque안에 있는 값들을 왼쪽으로 한칸씩 이동 0번째 인덱스에 있는 값은 가장 마지막 인덱스로 이동

print(deque[0]) 