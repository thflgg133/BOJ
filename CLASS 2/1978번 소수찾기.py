import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
answer = 0

for num in num_list:
    cnt = 0

    if num == 1: # 1은 소수가 아니므로 패스
        continue

    for i in range(2,num): # 소수 : 약수가 1과 자기 자신 밖에 없는 수
        if num % i == 0:  # num이 i로 나누어진다면 소수가 아니므로 cnt += 1 
            cnt += 1
            
    if cnt == 0: # i로 나누어지지 않았으므로 answer += 1 
        answer += 1 

print(answer)