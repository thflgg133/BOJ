import sys

def isPromise(x): # 윗줄의 퀸의 라인과 겹치는지 확인하는 함수
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i: # 수직 체크 & 대각선 체크{abs(행에서의 거리 차) == 열에서의 거리 차}
            return False 
    return True 


def dfs(x):
    global cnt

    if x == N:
        cnt += 1

    else:
        for i in range(N): # 열마다 퀸을 놓으면서 확인한다
            chess[x] = i
            if isPromise(x): 
                dfs(x+1) # 해당하는 열에 퀸을 놓을 수 있다면 다음 행으로 이동

N = int(sys.stdin.readline())
chess = [0 for i in range(16)] # 1 <= N <= 15
cnt = 0
dfs(0)
print(cnt)