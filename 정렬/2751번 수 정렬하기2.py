import sys

N = int(input())
list = []

for _ in range(N):
    list.append(int(sys.stdin.readline()))

list.sort()
for i in range(len(list)):
    sys.stdout.write(str(list[i])+'\n')

