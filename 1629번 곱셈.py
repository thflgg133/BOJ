import sys

def divide_and_conquer(num, n):
    if n == 1:
        return num % C
    
    if n % 2 == 0:
        y = divide_and_conquer(num, n//2)
        return y * y % C
    
    else:
        y = divide_and_conquer(num, (n-1)//2)
        return y * y * num % C


A, B, C = map(int, sys.stdin.readline().split())
print(divide_and_conquer(A,B))