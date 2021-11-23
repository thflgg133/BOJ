import sys

# 분할정복 -> 시간복잡도 O(logN)
def Dac(num,n):
    if n == 1:
        return num % C

    if n % 2 == 0:
        y = Dac(num,n//2)
        return y * y % C

    else:
        y = Dac(num,(n-1)//2)
        return y * y * num % C


A, B, C = map(int, sys.stdin.readline().split())
print(Dac(A,B))

# pow() 함수 이용 -> 시간복잡도 O(n)
print(pow(*map(int, sys.stdin.readline().rstrip().split())))