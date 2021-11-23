import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()

sum = 0
cnt = N

for i in range(N):
    sum += p[i]*cnt
    cnt -= 1

print(sum)
