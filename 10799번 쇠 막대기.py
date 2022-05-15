import sys

arr = list(sys.stdin.readline().rstrip())
ans = 0
stack = []

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
        
    # ')' -> 레이저 생성
    else:
        # 지금까지 겹처진 막대기 조각들 => +len(stack)
        if arr[i-1] == '(':
            stack.pop()
            ans += len(stack)
       
        # 막대기의 끝 => +1    
        else:
            stack.pop()
            ans += 1

print(ans)