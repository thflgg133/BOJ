'''
import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M= int(sys.stdin.readline())
card_cnt = list(map(int, sys.stdin.readline().split()))

hashmap = {}
for n in card:
    if n in hashmap:
        hashmap[n] += 1

    else:
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

card = Counter(card)
for i in card_cnt:
    print(card[i], end = " ")