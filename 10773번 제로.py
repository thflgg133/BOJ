import sys

K = int(sys.stdin.readline())
zero_list = []

for _ in range(K):
    num = int(input())
    
    if num == 0: # 0이 입력으로 돌아올 때 마다 pop() 함수를 이용해 가장 최근에 들어온 수 제거
        zero_list.pop()

    else:
        zero_list.append(num)

print(sum(zero_list)) 