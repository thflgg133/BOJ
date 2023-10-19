import sys

N = int(sys.stdin.readline())
tmp = [0]*10001

for _ in range(N):
    tmp[int(sys.stdin.readline())] += 1

for i in range(10001):
    if tmp[i] != 0:
        for j in range(tmp[i]):
           print(i)