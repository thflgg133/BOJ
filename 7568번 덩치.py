N = int(input())
list = []
for person in range(N):
    x,y = map(int, input().split())
    list.append((x,y))


for p1 in list:
    rank = 1

    for p2 in list:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            rank += 1

    print(rank, end = " ")