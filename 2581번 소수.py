M = int(input())
N = int(input())

num_list = [num for num in range(M,N+1)]
prime_num_list = []

for i in num_list:
    cnt = 0

    if i <= 1:
        continue
    
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1 

    if cnt == 0:
        prime_num_list.append(i)

if prime_num_list == []:
    print(-1)

else:
    print(sum(prime_num_list))
    print(min(prime_num_list))