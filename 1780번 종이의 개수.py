import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_one = 0
zero = 0
one = 0

def clip_paper(x, y, n):
    global zero, one, min_one

    check_num = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (paper[i][j] != check_num):
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n//3, y + l * n//3, n//3)
                    
                return

    if check_num == -1:
        min_one += 1

    elif check_num == 0:
        zero += 1

    else:
        one += 1 

clip_paper(0, 0, N)
print(min_one)
print(zero)
print(one)