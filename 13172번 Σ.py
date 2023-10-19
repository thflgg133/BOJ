import sys
import math
mod = int(1e9+7)

# 분할 정복
def Divide_and_Conquer(num, exp):
    if exp == 1: # 기댓값이 1 이면 
        return num

    if exp % 2 == 0:
        half = Divide_and_Conquer(num, exp//2)
        return half * half % mod

    else:
        return num * Divide_and_Conquer(num, exp-1) % mod


M = int(sys.stdin.readline())
total = 0

for _ in range(M):
    N, S = map(int, sys.stdin.readline().split())
    gcd = math.gcd(N, S) # 최대공약수
    N //= gcd
    S //= gcd

    total +=  S * Divide_and_Conquer(N, mod-2) % mod
    total %= mod

print(total)