import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = sys.stdin.readline().rstrip()
    print(arr[0]+arr[-1])