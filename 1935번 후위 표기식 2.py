import sys

N = int(sys.stdin.readline())
opr = ['*', '/', '+', '-'] # 연산자 종류 정의

current = sys.stdin.readline().rstrip()
num_list = [int(sys.stdin.readline()) for num in range(N)]
stack = []

for current in current:
    # 연산자가 아니면 ord()함수를 이용해 해당하는 수를 스택에 넣어준다.
    if current not in opr:
        stack.append(num_list[ord(current)-ord('A')])

    else:
        # 연산순서를 위해 변수에 각각 할당해줘서 계산한다.
        back = stack.pop()
        front = stack.pop()
        
        if current == '*':
            stack.append(front * back)
            
        if current == '/':
            stack.append(front / back)
        
        if current == '+':
            stack.append(front + back)
        
        if current == '-':
            stack.append(front - back)

print("{:.2f}".format(*stack))