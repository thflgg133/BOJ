import sys

def calender(M, N, x, y):
    # 마지막해는 M 과 N의 최소공배수 이므로 최대 M * N 까지 범위를 가진다
    while x <= M * N: 
        # x에 M을 계속 더해나간 값 = y에 N을 계속 더해나간 값 일때 정답 따라서 (x-y) % N == 0 이 성립해야 함             
        if (x-y) % N == 0: 
            return x     
        
        x += M

    return -1 # 존재 하지 않는 경우


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    # x는 x+M 번째 마다 돌아온다 x번째(x,?) -> x+M번째(x+M,?) -> x+M+M번째(x+M+M,?)
    # y는 y+N 번째 마다 돌아온다 y번째(?,y) -> y+N번째(?,y+N) -> y+N+N번째(?,y+N+N)
    print(calender(M, N, x, y))