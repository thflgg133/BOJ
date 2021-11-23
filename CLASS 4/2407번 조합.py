import sys
from math import factorial

n, m = map(int, sys.stdin.readline().split())
print((factorial(n) // factorial(n-m)) // factorial(m)) # factorial 함수 이용