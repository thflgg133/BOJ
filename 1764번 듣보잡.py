import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

hear_people = [sys.stdin.readline().rstrip() for i in range(N)]
see_people = [sys.stdin.readline().rstrip() for i in range(M)]

hear_see_people = list(set(hear_people) & set(see_people))

print(len(hear_see_people))
for name in sorted(hear_see_people):
    print(name)