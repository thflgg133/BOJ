import sys
from collections import defaultdict
# 딕셔너리 안에 key값이 없어도 에러가 나지 않고 설정된 값으로 key값이 초기화 됨

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
B_list = list(map(int, sys.stdin.readline().split()))

sum_A = defaultdict(int)
sum_B = defaultdict(int)


# 만들어 질 수 있는 수, 만들어지는 횟수를 모두 구해줌
for i in range(n):
    for j in range(i, n):
        sum_A[sum(A_list[i:j+1])] += 1


for i in range(m):
    for j in range(i, m):
        sum_B[sum(B_list[i:j+1])] += 1


ans = 0
for key in sum_A.keys():
    # B의 key값은 타겟 넘버가 될 수 있는 경우의 수를 나타낸다
    ans += sum_B[T - key] * sum_A[key]

print(ans)