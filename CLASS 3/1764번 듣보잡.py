import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

hear_people = [sys.stdin.readline().rstrip() for i in range(N)] # 듣도 못한 사람 명단
see_people = [sys.stdin.readline().rstrip() for i in range(M)] # 보도 못한 사람 명단

hear_see_people = list(set(hear_people) & set(see_people)) # set함수의 교집합 & 을 활용하여 듣도 보도 못한 사람을 구한다

print(len(hear_see_people))
print(*sorted(hear_see_people), sep='\n')