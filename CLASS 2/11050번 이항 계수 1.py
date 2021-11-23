from math import factorial
N, K = map(int, input().split())
binoary = factorial(N) // (factorial(K) * factorial(N - K))
print(binoary)