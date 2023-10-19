N = int(input())
num_list = list(map(int, input().split()))
answer = 0

for num in num_list:
    cnt = 0

    if num == 1:
        continue

    for i in range(2,num):
        if num % i == 0:
            cnt += 1
            
    if cnt == 0:
        answer += 1

print(answer)   

        