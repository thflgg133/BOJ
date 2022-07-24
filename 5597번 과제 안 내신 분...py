import sys

arr = []
for _ in range(28):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(1,31):
    if i not in arr:
        print(i)