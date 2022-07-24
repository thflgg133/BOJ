import sys

A, B = map(int, sys.stdin.readline().split())
ans = 0

ans = A+B
ans *= A-B
print(ans)