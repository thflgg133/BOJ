import sys

N = int(sys.stdin.readline())
meeting_time = []

for _ in range(N):
    start_time, end_time = map(int, sys.stdin.readline().split())
    meeting_time.append((start_time, end_time))

meeting_time = sorted(meeting_time, key=lambda t:t[0])
meeting_time = sorted(meeting_time, key=lambda t:t[1])
print(meeting_time)
last_time = 0
cnt = 0

for i, j in meeting_time:
    if i >= last_time:
        cnt += 1
        last_time = j

print(cnt)