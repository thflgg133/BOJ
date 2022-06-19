import sys

N = int(sys.stdin.readline())
circles = []

for idx in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x-r, x+r)) # 원의 시작과 끝을 담는다

circles.sort() # 순차적으로 정렬

for i in range(N-1):
    # 앞에서 부터 두 원을 비교함
    c1_left, c1_right = circles[i]
    c2_left, c2_right = circles[i+1]

    if c1_left == c2_left or c1_right == c2_right or c2_left < c1_right < c2_right: # 원이 내접, 외접, 두점에서 만날시 "NO" 출력
        print("NO")
        exit()

print("YES")