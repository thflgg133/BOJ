import sys

zero = [1,0] # 0이 출력되는 횟수 
one = [0,1] # 1이 출력되는 횟수

# 피보나치는 구하려는 수의 한단계 전과 두단계 전 수의 합이므로, 0 과 1의 개수도 한단계 전과 두단계 전에서 나오는 개수를 더하면 된다
for i in range(2,41): 
    zero.append(zero[i-1] + zero[i-2])
    one.append(one[i-1] + one[i-2])

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())    
    print(zero[N], one[N])