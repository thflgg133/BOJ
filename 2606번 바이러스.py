import sys

def dfs(start, computer):
    for i in computer[start]: 
        if i not in visit: # 이미 감염된 노드면 지나감
            visit.append(i) # 방문처리
            dfs(i, computer) # 감연된 노드부터 다시 탐색 시작


computer = {}
visit = []

for i in range(int(sys.stdin.readline())):
    computer[i+1] = [] 
    
for j in range(int(sys.stdin.readline())):
    num1, num2 = map(int, sys.stdin.readline().split())
    computer[num1].append(num2) # 양 방향이므로 입력받은 num1, num2 서로 연결
    computer[num2].append(num1) # 양 방향이므로 입력받은 num2, num1 서로 연결

dfs(1, computer) # 1번 컴퓨터부터 탐색
print(len(visit) - 1)