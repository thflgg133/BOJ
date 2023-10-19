import sys

string = sys.stdin.readline().rstrip()
explosion = list(sys.stdin.readline().rstrip())

stack = []

for i in range(len(string)):
    stack.append(string[i])
    
    # 시간 단축을 위해 stack에 마지막으로 들어온 문자랑 비교를 한다
    if stack[-1] == explosion[-1] and len(stack) >= len(explosion):
        if stack[-len(explosion):] == explosion: # 문자열 폭발!
            stack[-len(explosion):] = []
            
if stack:
    print(''.join(stack))
    
else:
    print("FRULA")