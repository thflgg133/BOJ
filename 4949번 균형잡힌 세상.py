import sys

while True: 

    s = sys.stdin.readline().rstrip()
    if s == '.': # .이 입력으로 들어오기전까지 while문 반복
        break

    string = []
    state = True 
    for i in s:
        if i == '(' or i == '[': # 괄호와 '.' 을 제외한 나머지 문자는 고려X
            string.append(i)

        elif i == ')':
            if string == [] or string[-1] == '[': # string이 비었거나 string에 가장 마지막에 들어간 값이 '(' 이 아닌 '[' 일 때
                state = False # 균형이 일어나지 않으므로 state = False
                break 

            elif string[-1] == '(': 
                string.pop() # 균형을 이루었으므로 string안의 '(' 를 pop하여 제거

        elif i == ']':
            if string == [] or string[-1] == '(': # 위와 같은 방법
                state = False
                break

            elif string[-1] == '[':
                string.pop()

    if state == True and string == []: # 위 조건을 만족하면 yes 출력
        print('yes')
        
    else:
        print('no')