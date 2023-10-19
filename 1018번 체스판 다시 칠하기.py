import sys

N, M = map(int, sys.stdin.readline().split())
chess = [sys.stdin.readline().rstrip() for _ in range(N)] # 체스판 형성
min_cnt = []  

for i in range(N-7): # 브루트포스 알고리즘 이용, 체스판 8x8 크기가 나올 수 있는 모든 경우의 수 탐색
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i+8): # 첫 칸을 검정색 기준으로 두고 검사하는 경우
            for l in range(j, j+8): 
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

        for k in range(i, i+8): # 첫 칸을 흰색 기준으로 두고 검사하는 경우
            for l in range(j, j+8):
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

        min_cnt.append(min(cnt1, cnt2)) # 두 케이스를 비교해 적은 값을 append

print(min(min_cnt)) # 가장 작은 값 출력