import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    # 위에서 때는 경우, 아래서 때는 경우를 나눠서 구한다
    for i in range(1, N): 
        # i가 1일때는 왼쪽 대각선에 붙어 있는 스티커는 때지지 않으므로 점수에 더한다
        if i == 1:
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]

        else:
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

    print(max(sticker[0][N-1], sticker[1][N-1]))