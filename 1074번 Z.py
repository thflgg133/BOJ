import sys

N, r, c = map(int, sys.stdin.readline().split())
result = 0

while True:
    if N < 1: # 더 이상 쪼개지지 않으므로 종료
        break

    middle = (N-1) ** 2 # 2^N X 2^N 의 중앙

    if r >= middle: 
        if c >= middle: # 오른쪽 아래 구역
            result += ((N-1) ** 4) * 3
            r -= middle
            c -= middle

        else: # 왼쪽 아래 구역
            result += ((N-1) ** 4) * 2
            r -= middle

    else:
        if c >= middle: # 오른쪽 위 구역
            result += ((N-1) ** 4) * 1
            c -= middle

        else: # 왼쪽 위 구역
            pass 

    N -= 1

if r == 0:
    if c == 0:
        print(result) # 왼쪽 위 구역

    else:
        print(result+1) # 오른쪽 위 구역

else:                                           
    if c == 0:
        print(result+2) # 왼쪽 아래 구역

    else:
        print(result+3) # 오른쪽 아래 구역