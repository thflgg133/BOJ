import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = list(sys.stdin.readline())

answer = 0
cnt = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I": # IOI가 탐색될때마다 cnt += 1
        cnt += 1

        if cnt == N: # N == 1 -> IOI, N == 2 -> IOIOI, N == 3 -> IOIOIOI ...
            cnt -= 1
            answer += 1 

        i += 1

    else:
        cnt = 0

    i += 1

print(answer)