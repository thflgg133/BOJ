import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
answer = 0

for _ in range(N):
    coin.append(int(sys.stdin.readline()))

coin.sort(reverse=True)

for i in range(len(coin)):
    if K // coin[i] != 0:
        answer += K // coin[i]
        K %= coin[i]
    
    if K == 0:
        break

print(answer)