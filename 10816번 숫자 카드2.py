'''
import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card_cnt = list(map(int, sys.stdin.readline().split()))

hashmap = {} # 해시를 이용한 풀이
for n in card:
    if n in hashmap: # 이미 카운트 된 수 일때  
        hashmap[n] += 1

    else: # 처음 카운트 될 경우
        hashmap[n] = 1

for m in card_cnt:
    if m in hashmap: 
        print(hashmap[m], end = " ")
    
    else:
        print(0, end = " ")

'''
from collections import Counter
import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M= int(sys.stdin.readline())
card_cnt = list(map(int, sys.stdin.readline().split()))

card = Counter(card) # Counter 함수를 통해 각각의 숫자가 몇 개씩 있는지 세준다
print(card)
for i in card_cnt:
    print(card[i], end = " ")