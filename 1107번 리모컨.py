import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if M: # 고장난 버튼이 있을때
    broken_buttons = sys.stdin.readline().split()

else:
    broken_buttons = []


cnt = abs(100 - N)

for channel in range(1000001):
    for i in str(channel):
        if i in broken_buttons:
            break

    else:
        cnt = min(cnt, len(str(channel)) + abs(channel - N))

print(cnt)