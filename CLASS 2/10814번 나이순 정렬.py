import sys

people = []

for _ in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().split()
    people.append((int(age), name))

# people.sort() sort()함수를 사용하면 나이 뿐만 아니라 이름의 알파벳 순으로도 정렬되기 떄문에 lambda를 사용한다
people.sort(key=lambda people: people[0]) # lambda 함수를 사용하여 age를 기준으로만 정렬

for i in range(len(people)):
    print(people[i][0], people[i][1])