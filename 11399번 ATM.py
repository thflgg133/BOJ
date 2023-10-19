import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort() # 시간의 합의 최솟값을 출력해야하므로 정렬

sum = 0
cnt = N

for i in range(N):
    sum += p[i] * cnt #첫번째 사람은 총인원수 만큼 더해지고 두번째 사람은 총인원수-1 만큼 더해지는 형식
    cnt -= 1

print(sum)
