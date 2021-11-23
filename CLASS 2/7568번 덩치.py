import sys

people = []
for person in range(int(sys.stdin.readline())):
    x,y = map(int, input().split())
    people.append([x,y])

# 첫 사람부터 한 명씩 차례대로 다른사람이랑 비교
for p1 in people:
    rank = 1 

    for p2 in people:
        if p1[0] < p2[0] and p1[1] < p2[1]: # 자신보다 키와 몸무게가 높은 사람이 있다면 덩치가 더 작은 것이므로 rank += 1
            rank += 1

    print(rank, end = " ")