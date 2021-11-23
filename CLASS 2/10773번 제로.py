K = int(input())
zero_list = []

for _ in range(K):
    num = int(input())
    
    if num == 0:
        zero_list.pop()

    else:
        zero_list.append(num)

print(sum(zero_list)) 