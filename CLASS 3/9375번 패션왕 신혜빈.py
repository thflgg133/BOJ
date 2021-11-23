import sys
from collections import Counter


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    type_list = []

    for _ in range(n):
        clothes, type = sys.stdin.readline().split()
        type_list.append(type)
    
    num = 1
    answer = Counter(type_list) #hash로 가능
    
    for key in answer:
        num *= answer[key] + 1

    print(num-1)            