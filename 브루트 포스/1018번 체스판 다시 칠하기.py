N, M = map(int, input().split())
chess = []
min_cnt = []
for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if k % 2 == 0 and l % 2 == 0:
                    if chess[k][l] == "W":
                        cnt1 += 1

                elif k % 2 == 1 and l % 2 == 1:
                    if chess[k][l] == "W":
                        cnt1 += 1 

                elif k % 2 == 0 and l % 2 == 1:
                    if chess[k][l] == "B":
                        cnt1 += 1

                elif k % 2 == 1 and l % 2 == 0:
                    if chess[k][l] == "B":
                        cnt1 += 1

        for k in range(i,i+8):
            for l in range(j,j+8):
                if k % 2 == 0 and l % 2 == 0:
                    if chess[k][l] == "B":
                        cnt2 += 1

                elif k % 2 == 1 and l % 2 == 1:
                    if chess[k][l] == "B":
                        cnt2 += 1 

                elif k % 2 == 0 and l % 2 == 1:
                    if chess[k][l] == "W":
                        cnt2 += 1

                elif k % 2 == 1 and l % 2 == 0:
                    if chess[k][l] == "W":
                        cnt2 += 1

        min_cnt.append(min(cnt1, cnt2))

print(min(min_cnt))