import sys
from collections import deque


def round(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


def main():
    n = int(sys.stdin.readline())
    
    if n == 0:
        res = 0
        
    else:
        score = deque(sorted([int(sys.stdin.readline()) for i in range(n)]))
        
        for i in range(round(n * 0.15)):
            score.popleft()
            score.pop()
            
        res = round(sum(score) / len(score))
        
    print(res)

ㄴ
if __name__ == "__main__":
    main()