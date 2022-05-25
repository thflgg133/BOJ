import sys
from itertools import combinations
import copy

expression = list(sys.stdin.readline().rstrip())
stack = []
cases = []
ans = set() # 중복 방지

for i in range(len(expression)):
    # '(' 이면 현재를 기준으로 두고 탐색 시작
    if expression[i] == '(':
        stack.append(i)
        
    # '(' 에 대응되는 쌍을 찾았으므로 쌍을 cases에 넣어줌
    elif expression[i] == ')':
        cases.append([stack.pop(), i])
       

for i in range(1, len(cases)+1):
    # combination 조합 최소 1개부터 ~ 최대 len(cases)개 까지
    case = combinations(cases, i)

    for j in case:
        # copy를 통해 수식 복사
        tmp = copy.copy(expression)
        
        # 이루는 괄호의 쌍들을 제거함
        for target in j:
            start, end = target
            tmp[start] = ''
            tmp[end] = ''
        
        # 제거된 수식 저장    
        ans.add(''.join(tmp))

# 사전순으로 출력
for current in sorted(ans):
    print(current)