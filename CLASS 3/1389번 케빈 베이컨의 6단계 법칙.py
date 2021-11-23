# BFS
import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
realationship = [[] for i in range(N+1)] # 노드끼리 연결되어 있다는걸 보여줄 배열 생성

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    realationship[A].append(B) # 이어지는 노드끼리 연결
    realationship[B].append(A) # 이어지는 노드끼리 연결


def bfs(realationship, start_node): #keypoint BFS
    num = [0] * (N+1) # 각각 노드가 몇번의 케빈 베이컨인지 측정을 위해 구현
    q = deque() #deque를 이용해 시간복잡도 줄임, q.pop(0)로 하면 구현은 되지만 시간이 길어짐
    visited[start_node] = 1 #일단 들어온 노드는 방문처리
    q.append(start_node) # 검증 시작

    while q:
        a = q.popleft() 

        for i in realationship[a]: #realationship[1] 일때 i = 3,4
            if visited[i] == 0: # 방문하지 않은 노드일 때
                num[i] = num[a] + 1 # i번 노드를 방문하기 위해 몇번 거쳤는지 추가 -->  가장 중요한 코드 ,  num[a] 는 이미 방문한 노드 이므로 + 1
                q.append(i) # realationship[a] 와 연결된 노드들 q에 추가
                visited[i] = 1 # 방문한 노드는 1로 처리해서 제외 시킴
                
    return sum(num) # 총 몇번 방문해서 케빈 베이컨을 만족했는지 return

result = []
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    result.append(bfs(realationship, i))

print(result.index(min(result))+1) # 1번째 부터니까 index + 1   