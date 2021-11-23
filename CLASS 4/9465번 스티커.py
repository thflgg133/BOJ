import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)] # 스티커 2줄

    for i in range(1,N):
        if i == 1: # i == 1 일때는 올 수 있는 방법이 1가지 이므로 현재 위치에 전 대각선 값을 더해준다.
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]

        else: # i != 1 일때는 i지점까지 올 수 있는 방법은 2가지이므로 두 가지 중 최댓값을 더해준다.
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

    print(max(sticker[0][N-1], sticker[1][N-1])) # 위에서 시작했을 때, 아래에서 시작했을 때 중 최댓값 출력