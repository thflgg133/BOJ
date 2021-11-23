import sys
from collections import deque

def bfs():
    queue = deque([1]) # 보드게임의 시작은 1번 칸부터
    
    while queue:
        
        marker = queue.popleft()

        for move in range(1,7): # 주사위의 눈 1 ~ 6 까지 각각 던졌을때 어디로 가는지 전부 따져보기 -> 그래야 최솟값을 판단할 수 있음!
            move_marker = move + marker # 원래 위치에서 주사위의 눈 만큼 이동

            if move_marker > 100: # 100을 넘으면 이동할 수 없으므로 패스
                continue

            num = game_board[move_marker] # 주사위를 던져서 이동한 위치의 칸
            visited[num] # 이동한 칸은 방문처리 하기 위한 코드

            if visited[num] == 0: # 처음 방문 했다면
                queue.append(num) # 도착한 칸을 다시 queue에 담음
                visited[num] = visited[marker] + 1 # 원래 칸에서 주사위를 1회 던져서 이동한 칸이므로 +1을 해줌
            
                if num == 100: # 100번째 칸에 도달하면 종료
                    return  


N, M = map(int, sys.stdin.readline().split())

game_board = [i for i in range(101)] # 게임보드판 형성 
                                     # 1~100 이지만 101칸을 만드는 이유? 1~100으로 하면 마지막 index value가 99이기 때문에

for _ in range(N): # 사다리
    x, y = map(int, sys.stdin.readline().split())
    game_board[x] = y 

for _ in range(M): # 뱀
    u, v = map(int, sys.stdin.readline().split())
    game_board[u] = v

visited = [0] * 101 # 특정 칸까지 도달하기 위해 주사위 던진 횟수를 파악하기 위한 코드
bfs() # bfs 탐색

print(visited[100]) 