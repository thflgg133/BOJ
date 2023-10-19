import sys
INF = sys.maxsize

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

# 투 포인터 왼쪽, 오른쪽 끝을 기준으로 잡고 탐색 시작
left, right = 0, N-1
min_diff = INF

while left < right:
    total = solutions[left] + solutions[right]
    
    # 절댓값 합이 0에 가까운 두 용액을 찾는다. 
    if abs(total) < min_diff:
        first, second = left, right
        min_diff = abs(total)        
    
    # 오름차순으로 용액들이 주어졌으므로 두 용액의 합이 0보다 크다면 오른쪽 포인터를, 0보다 작다면 왼쪽 포인터를 이동시킨다.    
    if total > 0:
        right -= 1
        continue
        
    elif total < 0:
        left += 1
        continue
        
    break
        
print(solutions[first], solutions[second])