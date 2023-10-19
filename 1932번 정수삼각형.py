import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(len(triangle[i])):
        if j == 0: # 제일 왼쪽 숫자
            triangle[i][j] += triangle[i-1][j]

        elif j == i: # 제일 오른쪽 숫자
            triangle[i][j] += triangle[i-1][j-1]

        else: # 왼쪽 대각선, 오른쪽 대각선 양쪽에서 올 수 있는 경우는 그 둘 중 큰 값을 넣는다
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1])) # 마지막 가지에서 최댓값 출력