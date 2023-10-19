import sys
from collections import deque

def bfs(A, B):
    queue = deque([[A, ""]]) # queue에 초기값 A와 커맨드가 입력될 빈문자열을 넣는다.
    visited = [False] * 10000 # 범위는 10000까지, D,S,L,R 명령을 통해 나온 숫자들을 방문 처리 하기 위한 공간 
    visited[A] = True # queue 에 들어온 A 값은 방문처리 / 방문처리 된 공간은 다시 방문할시 지나감

    while queue: 
        num, command = queue.popleft()

        if num == B: # 명령어를 실행한 후의 num이 최종값 B와 같다면 실행된 명령어들을 반환함
            return command

        # D
        if not visited[num * 2 % 10000]: # D 명령어를 실행한 후의 값이 아직 방문하지 않았을 때
            visited[num * 2 % 10000] = True # 방문 처리
            queue.append([num * 2 % 10000, command + "D"]) # D 명령어를 실행했으므로 바뀐 num값과 명령어 D을 queue에 삽입

        # S
        if not visited[(num - 1) % 10000]: # S 명령어를 실행한 후의 값이 아직 방문하지 않았을 때
            visited[(num - 1) % 10000] = True # 방문 처리
            queue.append([(num - 1) % 10000, command + "S"]) # S 명령어를 실행했으므로 바뀐 num값과 명령어 S을 queue에 삽입

        # L
        if not visited[num % 1000 * 10 + num // 1000]: # L 명령어를 실행한 후의 값이 아직 방문하지 않았을 때
            visited[num % 1000 * 10 + num // 1000] = True # 방문 처리
            queue.append([num % 1000 * 10 + num // 1000, command + "L"]) # L 명령어를 실행했으므로 바뀐 num값과 명령어 L을 queue에 삽입

        # R
        if not visited[num % 10 * 1000 + num // 10]: # R 명령어를 실행한 후의 값이 아직 방문하지 않았을 때
            visited[num % 10 * 1000 + num // 10] = True # 방문 처리
            queue.append([num % 10 * 1000 + num // 10, command + "R"]) # R 명령어를 실행했으므로 바뀐 num값과 명령어 R을 queue에 삽입


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().split())
    print(bfs(A, B))