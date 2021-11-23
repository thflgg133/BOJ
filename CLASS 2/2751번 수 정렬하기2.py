import sys

N = int(input())
list = []

for _ in range(N):
    list.append(int(sys.stdin.readline()))

list.sort() # 오름차순 정렬
for i in range(len(list)):
    print(list[i])