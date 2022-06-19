import sys

N, M = map(int, sys.stdin.readline().split())

words = {} # dictionary 사용
cnt = 0

for _ in range(N):
    S = sys.stdin.readline().rstrip()
    words[S] = 1 # 문자열 집합 S를 words안에 넣음
    
for _ in range(M):
    word = sys.stdin.readline().rstrip()

    if word in words: # 해당 단어가 words 안에 존재 시 cnt += 1 
        cnt += 1

print(cnt)