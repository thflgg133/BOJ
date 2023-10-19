N=int(input())
num=list(map(int, input().split()))

num_list=list(sorted(set(num)))
num_list={num_list[i]:i for i in range(len(num_list))}
print(*[num_list[i] for i in num]) 