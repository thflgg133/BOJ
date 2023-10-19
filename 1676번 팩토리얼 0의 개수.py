from math import factorial
import sys

N = int(sys.stdin.readline())
factorial_str = str(factorial(N))
cnt = 0

for i in range(len(factorial_str)-1,-1,-1):
    if factorial_str[i] == '0':
        cnt += 1

    
    if factorial_str[i] != '0':
        break

print(cnt)