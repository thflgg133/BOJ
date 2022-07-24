import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

cnt = 0
for num in arr:
    if num == v:
        cnt += 1
        
print(cnt)