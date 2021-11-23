import sys

T = int(sys.stdin.readline())

def calender(M, N, x, y):
    while x <= M * N: # 마지막해 -> M * N 번째, 이 전에 x,y 번째 해 존재
                      # x를 이용해 X에 M을 더할때마다 X는 그대로, y값이 변하는걸 이용 while y <= M*N도 상관X 
        if (x-y) % N ==0: # 찾는 번째 수는 x를 뺀 후 m으로 나누면 나머지가 0이다 동시에 y를 뺀 후 N으로 나누면 나머지가 0이다.
            return x     # 즉 x에 m을 계속 더해나간 값 = y에 n을 계속 더해나간 값 일때 정답 따라서 (x-y) % N ==0 이 성립해야 함
           
        
        x += M

    return -1 # 존재 하지 않는 경우


for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    # x는 x+M 번째 마다 돌아온다 x번째(x,?) -> x+M번째(x+M,?) -> x+M+M번째(x+M+M,?)
    # y는 y+N 번째 마다 돌아온다 y번째(?,y) -> y+N번째(?,y+N) -> y+N+N번째(?,y+N+N)
    print(calender(M, N, x, y))
    
    






