while True:

    s = input()
    if s == '.':
        break
    string = []
    tmp = True
    for i in s:
        if i == '(' or i == '[':
            string.append(i)

        elif i == ')':
            if string == [] or string[-1] == '[':
                tmp = False
                break

            elif string[-1] == '(':
                string.pop()

        elif i == ']':
            if string == [] or string[-1] == '(':
                tmp = False
                break

            elif string[-1] == '[':
                string.pop()

    if tmp == True and string == []:
        print('yes')
        
    else:
        print('no')