import sys

T = int(sys.stdin.readline())

for _ in range(T):
    case = sys.stdin.readline()
    sum = 0

    for i in case:
        if i == '(':
            sum += 1

        elif i == ')':
            sum += -1

        if sum < 0: # ')' 가 '(' 갯수보다 많이 나오면 더 이상 VPS가 아니기 때문에 NO 출력
            print("NO")
            break

    if sum > 0: # '(' 가 ')' 갯수보다 더 많이 나와 더 이상 VPS가 아니기 때문에 NO 출력
        print('NO')
    
    elif sum == 0: 
        print('YES')