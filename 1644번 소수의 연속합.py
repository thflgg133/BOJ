import sys
from math import sqrt

def isPrime(N):
    visited = [True for _ in range(N+1)]

    for i in range(2, int(sqrt(N))+1):
        if visited[i] == True:
            
            for j in range(i+i, N+1, i):
                visited[j] = False

    return [i for i in range(2, N+1) if visited[i] == True]
    

def two_pointer():
    cnt = 0
    start = 0
    end = 0

    while end <= len(prime_list):
        subtotal = sum(prime_list[start:end])

        # 소수의 부분합이 타겟 넘버일 때
        if subtotal == N:
            cnt += 1
            end += 1
        
        # 소수의 부분합이 타겟 넘버보다 작을 때
        elif subtotal < N:
            end += 1
        
        # 소수의 부분함이 타겟 넘버보다 클 때
        else:
            start += 1

    return cnt

N = int(sys.stdin.readline())
prime_list = isPrime(N)
print(two_pointer())