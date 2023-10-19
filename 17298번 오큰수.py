n = int(input())
nums = list(map(int, input().split()))
stack = []


ans = [-1 for _ in range(n)] # [-1, -1, -1, -1]
for i in range(n):
    # 스택이 비지 않았으면서, 다음수가 해당수보다 크면
    while stack and nums[stack[-1]] < nums[i]:
        # ans[(stack.pop()=현재 수에 해당하는 인덱스)]배열에 다음수 집어넣기
        ans[stack.pop()] = nums[i]
    stack.append(i)
    print(ans , stack)
print(*ans)