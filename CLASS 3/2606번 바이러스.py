import sys
computer = {}
visit = []


def dfs(start, dic):
    for i in dic[start]: # computer[1]
        if i not in visit:
            visit.append(i)
            dfs(i, dic)

for i in range(int(sys.stdin.readline())):
    computer[i+1] = list()

for j in range(int(sys.stdin.readline())):
    num1, num2 = map(int, sys.stdin.readline().split())
    computer[num1].append(num2)
    computer[num2].append(num1)

dfs(1,computer)
print(len(visit) - 1)