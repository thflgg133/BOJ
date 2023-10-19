import sys
INF = sys.maxsize

def next_cost(next, now):
    if now == 0:
        if next == 0:
            return 0

        else:
            return 2

    elif now == next:
        return 1

    elif (now - next) % 2 == 0:
        return 4

    else:
        return 3


move = list(map(int, sys.stdin.readline().split()))

# 처음으로 0이 들어오면 움직이지 않고 코드가 종료
if move[0] == 0:
    print(0)
    sys.exit()

move.pop()
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(move)+1)]
dp[-1][0][0] = 0

for i in range(len(move)):
    for left in range(5): # 왼발이 움직일 때
        for now in range(5):
            cost = next_cost(move[i], now) # 왼발이 현재 위치에서 move[i]로 움직임
            dp[i][move[i]][left] = min(dp[i][move[i]][left], dp[i-1][now][left] + cost)

    for right in range(5): # 오른발이 움직일 때
        for now in range(5):
            cost = next_cost(move[i], now) # 오른발이 현재 위치에서 move[i]로 움직임
            dp[i][right][move[i]] = min(dp[i][right][move[i]], dp[i-1][right][now] + cost)

ans = INF
for right in range(5):
    for left in range(5):
        ans = min(ans, dp[len(move)-1][right][left])

print(ans)