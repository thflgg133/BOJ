N = int(input())
list = []

for _ in range(N):
    x, y = map(int, input().split())
    list.append((x,y))

list.sort()
for x,y in list:
    print(x,y)