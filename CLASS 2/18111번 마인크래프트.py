import sys

N, M, B = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tall = 0
ans =  10000000000000

for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] < i:
                min += (i - ground[j][k])
                print(min)

            else:
                max += (ground[j][k] - i)

    inventory = max + B

    if inventory < min:
        continue

    time = 2 * max + min
    
    if time <= ans:
        ans = time
        tall = i

print(ans, tall)