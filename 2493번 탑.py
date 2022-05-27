import sys

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
ans = []

for now in range(N):
    while stack:
        # 마지막으로 추가된 타워의 높이가 현재 높이보다 높다면 ans에 넣어줌
        if stack[-1][1] > tower[now]:
            ans.append(stack[-1][0]+1)
            break
        
        # 현재의 높이보다 작은 타워들은 제거
        else:
            stack.pop()
         
    # 자신보다 높은 타워가 stack에 없다면 ans에 0을 넣어줌   
    if not stack:
        ans.append(0)
    
    # 현재 타워의 인덱스, 높이 를 stack에 넣어줌    
    stack.append([now, tower[now]])
    
print(*ans)