import sys

def clip_paper(x, y, n):
    global zero, one, min_one
    check_num = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != check_num: # 모든 종이가 같은 수로 되어 있지 않으므로 종이를 9등분 한다
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n//3, y + l * n//3, n//3)
                    
                return

    # 종이가 모두 같은 수로 되어있는 경우
    if check_num == -1:
        min_one += 1

    elif check_num == 0:
        zero += 1

    else:
        one += 1 


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_one, zero, one = 0, 0, 0

clip_paper(0, 0, N) # 제일 왼쪽 위 부터 탐색
print(min_one)
print(zero)
print(one)