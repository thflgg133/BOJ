import sys

N = int(sys.stdin.readline())
meeting_time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meeting_time = sorted(meeting_time, key=lambda t:[t[1], t[0]]) # 빨리 끝나는 회의 순서대로 정렬

last_time = 0 
cnt = 0

for i, j in meeting_time:
    # 회의 시작시간이 이전 회의 끝나는 시간보다 커야 배정이 가능
    if i >= last_time:
        cnt += 1
        last_time = j # 끝나는 시간을 갱신해줌

print(cnt)