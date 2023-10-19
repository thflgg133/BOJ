import sys
INF = sys.maxsize

N = int(sys.stdin.readline())

values = sorted(list(map(int, sys.stdin.readline().split())))
ans = INF
candidate = []

# 하나를 고정시키고 나머지 인덱스를 투 포인터를 이용해 구한다
for first in range(N-2):
    left, right = first+1, N-1
    
    while left < right:
        total = values[first] + values[left] + values[right]
        
        # 0에 가까운 특성값을 만들어야하기 때문에 abs()함수를 이용해 절댓값으로 비교한다.
        if abs(total) < abs(ans):
            second, third = left, right
            candidate = [values[first], values[second], values[right]]
            ans = total
            
        if total > 0:
            right -= 1
        
        elif total < 0 :
            left += 1
            
        else:
            print(*candidate)
            sys.exit()
             
print(*candidate)