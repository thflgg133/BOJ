import sys

def check(x): # 윗줄의 퀸의 라인과 겹치는지 확인하는 함수
    for i in range(x):
        # 같은 열인지 or 대각선에 퀸이 위치하는지 판단
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i: 
            return False
        
    return True 


def dfs(x):
    global cnt

    if x == N:
        cnt += 1

    else:
        for i in range(N): # 열마다 퀸을 놓으면서 확인한다
            chess[x] = i # x열 i칸에 퀸을 놓는다
            
            if check(x):
                dfs(x+1) # 다음 행으로 이동


N = int(sys.stdin.readline())
chess = [0 for i in range(16)] # 1 <= N <= 15
cnt = 0
dfs(0)
print(cnt)