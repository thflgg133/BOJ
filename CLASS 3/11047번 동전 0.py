import sys

N, K = map(int, sys.stdin.readline().split())
coin = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True) # 동전을 최소로 사용해야하므로 내림차순으로 정렬
print(coin)
answer = 0


for i in range(N):
    if K // coin[i] != 0: 
        answer += K // coin[i] # 금액을 동전으로 나눈 몫만큼 동전개수 더해짐
        K %= coin[i] # 몫으로 나누고 남은 나머지만큼 다시 for문을 통해 반복
    
    if K == 0:
        break

print(answer)   