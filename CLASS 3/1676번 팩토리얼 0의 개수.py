from math import factorial # factorial 함수를 쓰기 위해 import math
import sys

N = int(sys.stdin.readline())
factorial_str = str(factorial(N)) 
cnt = 0

for i in range(len(factorial_str)-1,-1,-1): # 0의 개수 탐색
    if factorial_str[i] == '0': # 0이면 cnt += 1
        cnt += 1
    
    else: # 0이 아니면 for 문 종료
        break

print(cnt)