import sys

string = list(sys.stdin.readline().rstrip())
stack = []
ans = 0
tmp = 1 

for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        tmp *= 2

    if string[i] == '[':
        stack.append(string[i])
        tmp *= 3


    if string[i] == ')':
        # 올바르지 않은 괄호열
        if not stack or stack[-1] == '[':
            ans = 0 
            break
        
        # 쌍을 이루면 ans에 지금까지의 tmp 값을 더해줌
        if string[i-1] == '(':
            ans += tmp
        
        stack.pop()
        tmp //= 2

    if string[i] == ']':
        # 올바르지 않은 괄호열
        if not stack or stack[-1] == '(':
            ans = 0
            break
        
        # 쌍을 이루면 ans에 지금까지의 tmp 값을 더해줌
        if string[i-1] == '[':
            ans += tmp
        
        stack.pop()
        tmp //= 3
    
if stack:
    print(0)

else:
    print(ans)