from itertools import product

N, M = map(int, input().split())

prod = list(product([i for i in range(1,N+1)], repeat=M))

for i in prod:
    print(*i)