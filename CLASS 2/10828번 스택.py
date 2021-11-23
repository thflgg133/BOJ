import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().split()
    order = cmd[0]


    if order == 'push':
        stack.append(cmd[1])

    if order == 'pop':
        if stack == []:
            print(-1)

        else:
            print(stack.pop())

    if order == 'size':
        print(len(stack))

    if order == 'empty':
        if stack == []:
            print(1)

        else:
            print(0)

    if order == 'top':
        if stack == []:
            print(-1) 

        else:
            print(stack[-1])
