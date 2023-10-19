import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
opeartor = list(map(int, sys.stdin.readline().split())) 
op_list = ["+","-","*","/"]
tmp = []

max_size = -1e9
min_size = 1e9

for i in range(len(opeartor)):
    for j in range(opeartor[i]):
        tmp.append(op_list[i])
           
for case in permutations(tmp, N-1):
    total = nums[0]
    for k in range(1, N):
        if case[k-1] == "+":
            total += nums[k]
            
        if case[k-1] == "-":
            total -= nums[k]
            
        if case[k-1] == "*":
            total *= nums[k]
            
        if case[k-1] == "/":
            total = int(total/ nums[k])
            
            
    if total > max_size:
        max_size = total
    if total < min_size:
        min_size = total

print(max_size)
print(min_size)