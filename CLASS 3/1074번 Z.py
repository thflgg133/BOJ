import sys

N, r, c = map(int, sys.stdin.readline().split())
result = 0

while True:
    if N < 1:
        break

    middle = 2 ** (N-1) # 2^N X 2^N 의 중앙

    if r >= middle:
        if c >= middle: # 4 사분면
            result += (4 ** (N-1)) * 3
            r -= middle
            c -= middle

        else: # 3 사분면
            result += (4 ** (N-1)) * 2
            r -= middle

    else:
        if c >= middle: # 2 사분면
            result += (4 ** (N-1)) * 1
            c -= middle

        else: # 1 사분면
            pass 
            
    N -= 1

    
if r == 0:
    if c == 0:
        print(result)

    else:
        print(result+1) 

else:
    if c == 0:
        print(result+2)

    else:
        print(result+3)

'''
# 재귀함수 형식

import sys

def divide(size, start_row, start_col):
    global cnt

    if size == 2:
        if start_row == r and start_col == c:  # 왼쪽 위
            print(cnt)
            sys.exit(0)

        if start_row == r and start_col + 1 == c:  # 오른쪽 위
            print(cnt + 1)
            sys.exit(0)

        if start_row + 1 == r and start_col == c:  # 왼쪽 아래
            print(cnt + 2)
            sys.exit(0)

        if start_row + 1 == r and start_col + 1 == c:  # 오른쪽 아래
            print(cnt + 3)
            sys.exit(0)
        
        cnt += 4

    else:
        if r <= start_row + size // 2 and c <= start_col + size // 2:
            divide(size // 2, start_row, start_col)

        else:
            cnt += (size // 2) ** 2

        if r <= start_row + size // 2 and c <= start_col + size // 2 * 2:
            divide(size // 2, start_row, start_col + size // 2)

        else:
            cnt += (size // 2) ** 2

        if r <= start_row + size // 2 * 2 and c <= start_col + size // 2:
            divide(size // 2, start_row + size // 2, start_col)

        else:
            cnt += (size // 2) ** 2

        if r <= start_row + size // 2 * 2 and c <= start_col + size // 2 * 2:
            divide(size // 2, start_row + size // 2, start_col + size // 2)
            
        else:
            cnt += (size // 2) ** 2


if __name__ == "__main__":

    N, r, c = map(int, sys.stdin.readline().split())

    cnt = 0
    divide(2 ** N, 0, 0)
'''