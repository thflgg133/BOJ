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
    answer = Counter(type_list) # 각 종류에 해당하는 옷 가지수를 Counter함수로 카운트
    
    for key in answer:
        num *= answer[key] + 1

    print(num-1)