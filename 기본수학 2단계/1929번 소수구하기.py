M, N = map(int, input().split())

for num in range(M, N+1):
    cnt = 0

    for i in range(2, int(num **0.5) + 1):
        if num % i == 0:
            cnt += 1 

    if cnt == 0:
        print(num)