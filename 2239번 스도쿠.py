import sys

# 가로에 겹치는 숫자가 있는지 체크
def check_row(row, num):
    for col in range(9):
        if puzzle[row][col] == num:
            return False
    
    return True

# 세로에 겹치는 숫자가 있는지 체크
def check_col(col, num):
    for row in range(9):
        if puzzle[row][col] == num:
            return False

    return True
    
# 3x3 구역안에 겹치는 숫자가 있는지 체크
def check_block(row, col, num):
    row = row//3 * 3
    col = col//3 * 3
    for i in range(3):
        for j in range(3):
            if puzzle[row+i][col+j] == num:
                return False

    return True
    

def dfs(n):
    if n == len(empty):
        for row in range(9):
            print(*puzzle[row], sep="")

        exit()
    
    x, y = empty[n]
    for num in range(1,10):
        if check_row(x, num) and check_col(y, num) and check_block(x, y, num):
            puzzle[x][y] = num
            dfs(n+1)
            puzzle[x][y] = 0


puzzle = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
empty = [(i,j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]
dfs(0)