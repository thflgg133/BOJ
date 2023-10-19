import sys
from collections import deque

def bfs(realationship, start_node): 
    num = [0] * (N+1) # 각각 노드가 몇번의 케빈 베이컨 수인지 측정을 위해 구현
    queue = deque([start_node]) # deque를 이용해 시간복잡도 줄임, q.pop(0)로 하면 구현은 되지만 시간이 길어짐
    visited[start_node] = 1 # 방문처리

    while queue:
        node = queue.popleft() 

        for i in realationship[node]:
            if not visited[i]: # 방문하지 않은 노드일 때
                num[i] = num[node] + 1 # i번 노드를 방문하기 위해 몇번 거쳤는지 추가 -->  가장 중요한 코드 ,  num[a] 는 이미 방문한 노드 이므로 + 1
                queue.append(i) 
                visited[i] = 1 # 방문처리
                
    return sum(num) # 총 몇번 방문해서 케빈 베이컨을 만족했는지 return


N, M = map(int, sys.stdin.readline().split())
realationship = [[] for i in range(N+1)] # 노드끼리 연결되어 있다는걸 보여줄 배열 생성

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    realationship[A].append(B)  
    realationship[B].append(A) 

result = []
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    result.append(bfs(realationship, i)) # 방문 수가 같을 때, 번호가 가장 작은 사람을 출력하기 위해 하나씩 순서대로 넣어줌

print(result.index(min(result))+1) # index는 0번째 부터 시작이므로 +1 해서 출력