import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().split()
    order = cmd[0] # 명령어


    if order == 'push':
        stack.append(cmd[1]) 

    if order == 'pop': # 스택에서 가장 위에 있는 수 제거 후 출력
        if stack == []: 
            print(-1) # 스택이 비어있을 시 -1 출력

        else:
            print(stack.pop())

    if order == 'size': # 스택의 사이즈 출력
        print(len(stack))

    if order == 'empty': # 스택이 비었는지 아닌지 판단
        if stack == []:
            print(1)

        else:
            print(0)

    if order == 'top': # 스택의 가장 위에 있는 수 출력
        if stack == []: # 스택이 비어있을 시 -1 출력
            print(-1) 

        else:
            print(stack[-1])
