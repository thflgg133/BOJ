import sys

def mulmatrix(m1, m2):
    tmp =  [[0] * N for _ in range(N)]

    # 행렬 곱 계산
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += m1[i][k] * m2[k][j]
            
            tmp[i][j] %= 1000 # 연산 속도를 높이기 위해 계속 1000으로 나눠준다
         
    return tmp


# 분할 정복
def devide(square, matrix):
    if square == 1:
        return matrix

    else:
        if square % 2 == 0:
            matrix = devide(square//2, matrix)
            return mulmatrix(matrix, matrix)

        else:
            matrix = devide(square-1, matrix)
            return mulmatrix(first_matrix, matrix)


N, B = map(int, sys.stdin.readline().split())
first_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for col in range(N):
    for row in range(N):
        print(devide(B, first_matrix)[col][row] % 1000, end =" ") 
    print()