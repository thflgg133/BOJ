N = int(input())
list = []

for _ in range(N):
    list.append(int(input()))

list.sort()
for i in range(len(list)):
    print(list[i])

