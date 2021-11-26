import sys
import math
mod = int(1e9+7) # 

def ExpectNum(num, exp):
    if exp == 1:
        return num

    if exp % 2 == 0:
        half = ExpectNum(num, exp//2)
        return half * half % mod

    else:
        return num * ExpectNum(num, exp-1) % mod


M = int(sys.stdin.readline())
total = 0

for _ in range(M):
    N, S = map(int, sys.stdin.readline().split())
    gcd = math.gcd(N, S) # 최대공약수
    N //= gcd
    S //= gcd

    total +=  S * ExpectNum(N, mod-2) % mod
    total %= mod


print(total)